# parquet-cli
Command line (CLI) tool to inspect Apache Parquet files on the go

`parq` is small script to easily preview Parquet files. It can show basic information needed for quick debugging.


## Install

`pip install parquet-cli`

An executable script called `parq` will be installed.

# Use

Get metadata and schema information:

`$ parq path/to/file.parquet`

```
 # Metadata
<pyarrow._parquet.FileMetaData object at 0x1014879a8>
created_by: parquet-mr version 1.8.1 (build 4aba4dae7bb0d4edbcf7923ae1339f28fd3f7fcf)
num_columns: 13
num_rows: 1000
num_row_groups: 1
format_version: 1.0
serialized_size: 1125

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

Get top N records (head)

`parq path/to/file.parquet --head 10`

Get bottom N records (tail)

`parq path/to/file.parquet --head 10`

Get total rows count:

`parq path/to/file.parquet --count`
