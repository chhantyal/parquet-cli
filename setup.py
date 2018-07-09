import sys
from setuptools import setup, find_packages

msg = "Command line (CLI) tool to inspect Apache Parquet files on the go"


def get_pyarrow_version():

    if sys.platform == "darwin":
        pyarrow = 'pyarrow>=0.9.0.post1'
    else:
        pyarrow = 'pyarrow>=0.9.0'
    return pyarrow


setup(
    name='parquet-cli',
    version='1.2',
    description=msg,
    long_description=msg,
    author='Nar Kumar Chhantyal',
    author_email='nkchhantyal@gmail.com',
    url='https://github.com/chhantyal/parquet-cli',
    license='BSD 3-Clause License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages(),
    platforms='any',
    install_requires=[
        'pandas==0.22.0',
        get_pyarrow_version()
    ],
    entry_points={
        'console_scripts': [
            'parq = parq.main:main',
        ]
    },
    package_data={'example': ['*.parquet']},
    include_package_data=True,
)
