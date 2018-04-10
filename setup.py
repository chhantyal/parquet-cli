
from setuptools import setup, find_packages

setup(
    name='parquet-cli',
    version='1.0',
    description='Command line (CLI) tool to inspect Apache Parquet files on the go',
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
        'pandas',
        'pyarrow'
    ],
    entry_points={
        'console_scripts': [
            'parq = parq.main:main',
        ]
    },
    package_data={'example': ['*.parquet']},
    include_package_data=True,
)
