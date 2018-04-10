from __future__ import print_function

import sys
import argparse

import pyarrow.parquet as pq


def get_metadata(parquet_file):
    r = pq.ParquetFile(parquet_file)
    return r.metadata


def get_schema(parquet_file):
    r = pq.ParquetFile(parquet_file)
    return r.schema


def get_data(pq_table, n, head=True):
    data = pq_table.to_pandas()
    if head:
        rows = data.head(n)
    else:
        rows = data.tail(n)
    return rows


def main(cmd_args=sys.argv, skip=False):
    """
    Main entry point with CLI arguments
    :param cmd_args: args passed from CLI
    :param skip: bool, whether to skip init_args call or not
    :return: string stdout
    """
    if not skip:
        cmd_args = init_args()

    pq_table = pq.read_table(cmd_args.file)
    if cmd_args.head:
        print(get_data(pq_table, cmd_args.head))
    elif cmd_args.tail:
        print(get_data(pq_table, cmd_args.tail, head=False))
    elif cmd_args.count:
        print(len(pq_table.to_pandas().index))
    elif cmd_args.schema:
        print("\n # Schema \n", get_schema(cmd_args.file))
    else:
        print("\n # Metadata \n", get_metadata(cmd_args.file))


def init_args():
    parser = argparse.ArgumentParser(
        description="Command line (CLI) tool to inspect Apache Parquet files on the go",
        usage="usage: parq file [-s [SCHEMA] | --head [HEAD] | --tail [TAIL] | -c [COUNT]]"
    )

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-s",
                       "--schema",
                       nargs="?",
                       type=bool,
                       const=True,
                       help="get schema information",
                       )

    group.add_argument("--head",
                       nargs="?",
                       type=int,
                       const=10,
                       help="get first N rows from file"
                       )

    group.add_argument("--tail",
                       nargs="?",
                       type=int,
                       const=10,
                       help="get last N rows from file"
                       )

    group.add_argument("-c",
                       "--count",
                       nargs="?",
                       type=bool,
                       const=True,
                       help="get total rows count",
                       )

    parser.add_argument("file",
                        type=argparse.FileType('rb'),
                        help='Parquet file')

    cmd_args = parser.parse_args()

    return cmd_args


if __name__ == '__main__':
    args = init_args()
    main(args, skip=True)
