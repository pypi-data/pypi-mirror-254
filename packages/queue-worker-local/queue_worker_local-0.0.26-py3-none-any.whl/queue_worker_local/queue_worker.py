import argparse
import json
import multiprocessing
import os
import random
import subprocess
import sys
import time
from io import StringIO

import requests
from database_mysql_local.generic_crud import GenericCRUD
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from logger_local.MetaLogger import MetaLogger
from queue_local.database_queue import DatabaseQueue
from user_context_remote.user_context import UserContext

QUEUE_WORKER_COMPONENT_ID = 159
QUEUE_WORKER_COMPONENT_NAME = 'queue_worker_local_python_package/src/queue_worker.py'
DEVELOPER_EMAIL = 'akiva.s@circ.zone'
logger_object = {'component_id': QUEUE_WORKER_COMPONENT_ID,
                 'component_name': QUEUE_WORKER_COMPONENT_NAME,
                 'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
                 'developer_email': DEVELOPER_EMAIL}

DELIMITER = "returned_value: "
installed = []  # to avoid installing the same package multiple times


class QueueWorker(DatabaseQueue, metaclass=MetaLogger, object=logger_object):
    """A queue worker that executes tasks from the queue.
    If the given table does not have the required columns, the results will be saved in the logger instead.
    """

    def __init__(self, schema_name: str = "queue", table_name: str = "queue_item_table",
                 view_name: str = "queue_item_view", id_column_name: str = "queue_item_id",
                 action_boolean_column: str = "is_queue_action", is_test_data: bool = False) -> None:
        super().__init__(schema_name=schema_name, table_name=table_name, view_name=view_name,
                         id_column_name=id_column_name, is_test_data=is_test_data)
        self.all_actions = self.get_all_actions(action_boolean_column)
        self.user = UserContext()
        self.save_in_logger = not self._table_has_required_columns()
        # TODO is this the best approach? We need it also in logger, right? What solution do we use in the logger? Can we move this to python-sdk?
        self.ip_v4 = requests.get('https://ipv4.seeip.org/jsonip').json()['ip']
        self.ip_v6 = requests.get('https://api.seeip.org/jsonip').json()['ip']

    def _get_action_ids(self, action_names: tuple) -> tuple:
        """Get the action IDs from the action names."""
        if not action_names:
            return ()
        return tuple(action["action_id"] for action in self.all_actions if action["action_name"] in action_names)

    def execute(self, action_ids: tuple = (), action_names: tuple = (),
                min_delay_after_execution_ms: float = 0.0,
                max_delay_after_execution_ms: float = 0.0,
                total_missions: int = 1,
                raise_on_error: bool = True,
                push_back_on_error: bool = False,
                install_packages: bool = True,
                working_directory: str | None = None,
                execution_details: dict = None
                ) -> int:
        """Execute tasks from the queue.

        If execution_details is provided, the queue will not be used.
        If provided, execution_details must contain the following columns:
            `id_column_name`, action_id, function_parameters_json, class_parameters_json"""

        if execution_details:
            requiered_columns = (self.id_column_name, "action_id",
                                 "function_parameters_json", "class_parameters_json")
            for column in requiered_columns:
                if column not in execution_details:
                    raise ValueError(f"Missing column {column} in execution_details.\n"
                                     f"Required columns: {requiered_columns}")
        action_ids += self._get_action_ids(action_names)
        if install_packages:
            self._install_packages(action_ids)
        max_delay_after_execution_ms = max(max_delay_after_execution_ms, min_delay_after_execution_ms)
        status_code = 0
        last_user_jwt = None
        for mission in range(total_missions):
            if execution_details:
                queue_item = execution_details
            else:
                queue_item = self.get(action_ids=action_ids)
            if not queue_item:
                self.logger.info(f'The queue does not have more items of action_ids {action_ids}')
                break

            function_parameters = json.loads(queue_item["function_parameters_json"] or "{}")
            class_parameters = json.loads(queue_item["class_parameters_json"] or "{}")
            formatted_function_params = ', '.join(
                [f'{key}={repr(value)}' for key, value in function_parameters.items()])

            action = self.get_action(queue_item)
            filename = action["filename"]
            function_name = action["function_name"]

            if filename.endswith('.py'):
                args = self._get_python_args(action, class_parameters, function_parameters)
            # elif...
            else:
                error_message = f"Unsupported file extension {filename} for action {queue_item['action_id']}"
                raise Exception(error_message)

            self.logger.info(f'Executing the following shell script: {" ".join(args)}')
            current_thread_id = get_thread_id()
            print(f"{queue_item['action_id']}, {os.getpid()}, {current_thread_id}")
            if last_user_jwt != queue_item.get("user_jwt"):
                self.user.login_using_user_jwt(queue_item["user_jwt"])
                last_user_jwt = queue_item["user_jwt"]

            stdout = stderr = returncode = None
            if filename.endswith('.py'):
                try:
                    # we prefer using exec as it is faster
                    stdout, stderr, returncode = self.execute_python_script(args)
                except ImportError:
                    self.logger.warning(f"Failed to execute {function_name}({formatted_function_params}) with exec()"
                                        f" retrying using subprocess.run()")

            if returncode is None:  # retry or not python
                result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                        text=True, cwd=working_directory)
                returncode = result.returncode
                stdout = result.stdout
                stderr = result.stderr

            print(f"{queue_item['action_id']}, {os.getpid()}, {current_thread_id}, {returncode}")

            self.save_execution_result(queue_item[self.id_column_name], stdout, stderr, returncode,
                                       session_id=queue_item.get("session_id"))

            if not stderr:
                self.logger.info(f'Successfully executed {function_name}({formatted_function_params})')
            else:
                error_message = f'Error while executing {function_name}({formatted_function_params}):\n{stderr}\n'
                if push_back_on_error:
                    self.push_back(queue_item)
                status_code = 1
                if raise_on_error:
                    raise Exception(error_message)

            sleep_time = random.uniform(min_delay_after_execution_ms / 1000, max_delay_after_execution_ms / 1000)
            self.logger.info(f'Sleeping for {sleep_time} seconds')
            time.sleep(sleep_time)

        return status_code

    def execute_python_script(self, args: list) -> tuple:
        # Save the original stdout and stderr
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        # Create file-like objects to capture output
        stdout_capture = sys.stdout = StringIO()
        stderr_capture = sys.stderr = StringIO()
        try:
            exec(args[-1])  # We are using our scripts, so it is safe to execute them
            returncode = 0
        except Exception as e:
            self.logger.exception("An error occurred during execution:", object=e)
            returncode = 1
        finally:
            # Restore the original stdout and stderr
            sys.stdout = original_stdout
            sys.stderr = original_stderr
        # Get the captured output
        stdout = stdout_capture.getvalue()
        stderr = stderr_capture.getvalue()
        return stdout, stderr, returncode

    def save_execution_result(self, queue_item_id: int, stdout: str, stderr: str, returncode: int,
                              session_id: str = None):
        """Save the execution result in the database or in the logger."""

        if DELIMITER in stdout:
            stdout, returned_value = stdout.split(DELIMITER)
        else:
            returned_value = None
        return_message = "Success" if not stderr else "Error"
        data_json = {"stdout": stdout, "stderr": stderr, "return_code": returncode,
                     "return_message": return_message, "returned_value": returned_value,
                     "server_ip_v4": self.ip_v4, "server_ip_v6": self.ip_v6, "thread_id": get_thread_id()}
        # TODO: add end_timestamp to the crud
        if self.save_in_logger:
            data_json["session"] = session_id
            old_schema_name = self.schema_name
            super().set_schema(schema_name="logger")
            super().insert(table_name="logger_table", data_json=data_json)  # don't use self.insert
            super().set_schema(schema_name=old_schema_name)
        else:
            super().update_by_id(id_column_value=queue_item_id, data_json=data_json)

    @staticmethod
    def _get_python_args(action: dict, class_parameters: dict, function_parameters: dict) -> list:
        """Get the arguments for the python command line."""
        class_parameters = class_parameters or {}  # in case it is None
        function_parameters = function_parameters or {}
        function_name = action["function_name"]
        filename = action["filename"].replace(".py", "")
        folder = (action["folder_name"] + ".") if action["folder_name"] else ""

        function_module = action["function_module"]

        if function_module:
            function_call = f"{function_module}(**{class_parameters}).{function_name}(**{function_parameters})"
        else:
            function_call = f"{function_name}(**{function_parameters})"
        command = f'from {folder}{filename} import {function_module or function_name}\n' + \
                  f'result = {function_call}\n' + \
                  f'print("{DELIMITER}" + ' + ' str(result or {}), end="")'
        return [sys.executable, '-c', command]

    def get_action(self, queue_item: dict) -> dict:
        """Get the action from the database."""
        try:
            return next(action for action in self.all_actions if action['action_id'] == queue_item['action_id'])
        except StopIteration:
            raise ValueError(f"No such action_id {queue_item['action_id']}")

    @staticmethod
    def get_all_actions(action_boolean_column: str) -> list:
        """Get all actions from the database."""
        all_actions = GenericCRUD(default_schema_name="action").select_multi_dict_by_id(
            # TODO Please replace all Magic Numbers with const enum i.e. 1 
            view_table_name="action_view", id_column_name=action_boolean_column, id_column_value=1)
        return all_actions

    def _install_packages(self, action_ids: tuple) -> None:

        for action in self.all_actions:
            if action["action_id"] not in action_ids or action["package_name"] in installed:
                continue
            filename = action["filename"]
            package_name = action["package_name"]

            if not filename or not package_name:
                continue
            if filename.endswith('.py'):
                try:
                    # hide the output
                    subprocess.check_call(["pip", "install", "-U", package_name], stdout=subprocess.DEVNULL)
                except subprocess.CalledProcessError as e:
                    self.logger.exception(f"Failed to install {package_name}", object=e)
                    continue
            elif filename.endswith(".ts"):
                subprocess.check_call(["npm", "install", package_name])
                subprocess.check_call(["npm", "update", package_name])
            # elif...
            installed.append(action["package_name"])

    def _table_has_required_columns(self) -> bool:

        required_columns = ("stdout", "stderr", "return_code", "return_message", "returned_value",
                            "server_ip_v4", "server_ip_v6", "thread_id")
        self.cursor.execute(f"SELECT column_name FROM information_schema.columns "
                            f"WHERE table_schema = '{self.schema_name}' AND table_name = '{self.default_table_name}' ")
        columns = [row[0] for row in self.cursor.fetchall()]
        has_required_columns = all(column in columns for column in required_columns)
        return has_required_columns


def execute_queue_worker(action_ids: tuple, action_names: tuple, min_delay_after_execution_ms: float,
                         max_delay_after_execution_ms: float, total_missions: int):
    queue_worker = QueueWorker()  # cannot share it between processes
    queue_worker.execute(action_ids, action_names, min_delay_after_execution_ms,
                         max_delay_after_execution_ms, total_missions)


def get_thread_id():
    """Returns the current thread ID"""
    return multiprocessing.current_process().ident


def main():
    """See README.md"""
    parser = argparse.ArgumentParser(description='Queue Worker')

    parser.add_argument('-min_delay_after_execution_ms', type=float, default=0.0)
    parser.add_argument('-max_delay_after_execution_ms', type=float, default=0.0)
    parser.add_argument('-action_ids', type=int, nargs='+', help='List of action IDs', default=())
    parser.add_argument('-action_names', type=str, nargs='+',
                        help='Action names in addition to the action IDs', default=())
    parser.add_argument('-total_missions', type=int, default=1,
                        help='Number of missions to execute')
    parser.add_argument('-raise_on_error', type=bool, default=True,
                        help='Whether to raise an exception on error')
    parser.add_argument('-push_back_on_error', type=bool, default=False,
                        help='Whether to push back the item to the queue when an error occurs')
    parser.add_argument('-processes', type=int, default=1, help='Number of processes to start')
    parser.add_argument('-install_packages', type=bool, default=True, help='Whether to install packages')
    parser.add_argument('-working_directory', type=str, default=os.path.dirname(os.path.abspath(__file__)),
                        help='The working directory of the queue worker')

    args = parser.parse_args()
    if not args.action_ids and not args.action_names:
        print("At least one of the following arguments must be provided: -action_ids, -action_names")
        return
    if any(x is None for x in vars(args).values()):
        print(f"Usage: python {__file__} -min_delay_after_execution_ms 0 -max_delay_after_execution_ms 1 "
              f"-action_ids 1 2 4 -total_missions 100 -processes 1")
        return

    processes = []
    try:
        for _ in range(args.processes):
            worker_args = (tuple(args.action_ids), tuple(args.action_names), args.min_delay_after_execution_ms,
                           args.max_delay_after_execution_ms, args.total_missions // args.processes)
            process = multiprocessing.Process(target=execute_queue_worker, args=worker_args)
            processes.append(process)

        # Start the processes
        for process in processes:
            process.start()

        # Wait for all processes to complete
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        for process in processes:
            process.terminate()


if __name__ == "__main__":
    main()
