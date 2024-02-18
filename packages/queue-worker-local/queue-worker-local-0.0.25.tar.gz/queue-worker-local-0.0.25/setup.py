import setuptools

PACKAGE_NAME = "queue-worker-local"
package_dir = PACKAGE_NAME.replace("-", "_")

setuptools.setup(
    name=PACKAGE_NAME,  # https://pypi.org/project/queue-worker-local
    version='0.0.25',
    author="Circles",
    author_email="info@circles.life",
    url=f"https://github.com/circles-zone/{PACKAGE_NAME}-python-package",
    packages=[package_dir],
    package_dir={package_dir: f'{package_dir}/src'},
    package_data={package_dir: ['*.py']},
    long_description="This is a package for sharing common crud operation to queue schema in the db",
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pytest>=7.4.1",
        "database-mysql-local>=0.0.116",
        "logger-local>=0.0.71",
        "queue-local>=0.0.23"]
)
