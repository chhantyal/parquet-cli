# parquet-cli
Command line (CLI) tool to inspect Apache Parquet files on the go

Apache Parquet is a columnar storage format commonly used in the Hadoop ecosystem.

`parq` is small, easy to install, Python utility to view and get basic information from Parquet files.

Current features set are what I need, please use Github issues for any requests/suggestions.

## Install

`pip install parquet-cli`

An executable script called `parq` will be installed.

# Use

Once installed, you can use `parq` command.

View Parquet file metadata:

`$ parq input.parquet`

```
# Metadata
<pyarrow._parquet.FileMetaData object at 0x1014879a8>
created_by: parquet-mr version 1.8.1 (build 4aba4dae7bb0d4edbcf7923ae1339f28fd3f7fcf)
num_columns: 13
num_rows: 1000
num_row_groups: 1
format_version: 1.0
serialized_size: 1125
```

Get schema information:

`$ parq input.parquet --schema`

```
# Schema
<pyarrow._parquet.ParquetSchema object at 0x1048b9a88>
registration_dttm: INT96
id: INT32
name: BYTE_ARRAY UTF8
email: BYTE_ARRAY UTF8
...
ip_address: BYTE_ARRAY UTF8
country: BYTE_ARRAY UTF8

```

Get total rows count:

`$ parq input.parquet --count`

```
1025
```

Get top N records (head)

`$ parq input.parquet --head 10`

Get bottom N records (tail)

`$ parq input.parquet --tail 10`


## Help

`$ parq --help`

```
usage: usage: parq file [-s [SCHEMA] | --head [HEAD] | --tail [TAIL] | -c [COUNT]]

positional arguments:
  file                  Parquet file

optional arguments:
  -h, --help            show this help message and exit
  -s [SCHEMA], --schema [SCHEMA]
                        get schema information
  --head [HEAD]         get first N rows from file
  --tail [TAIL]         get last N rows from file
  -c [COUNT], --count [COUNT]
                        get total rows count
```