from __future__ import print_function

import sys
import argparse

import pyarrow.parquet as pq


def summery(parquet_file):
    r = pq.ParquetFile(parquet_file)
    print("\n # Metadata \n", r.metadata)
    print("\n # Schema \n", r.schema)
    return {
        "schema": r.schema,
        "metadata": r.metadata
    }


def get_data(pq_table, n, head=True):
    data = pq_table.to_pandas()
    if head:
        rows = data.head(n)
    else:
        rows = data.tail(n)
    print(rows)
    return rows


def main(cmd_args=sys.argv, skip=False):
    """
    Main entry point with CLI arguments
    :param cmd_args: args passed from CLI
    :return: string stdout
    """
    if not skip:
        cmd_args = init_args()

    pq_table = pq.read_table(cmd_args.file)
    if cmd_args.head:
        get_data(pq_table, cmd_args.head)
    elif cmd_args.tail:
        get_data(pq_table, cmd_args.tail, head=False)
    elif cmd_args.count:
        print(len(pq_table.to_pandas().index))
    else:
        summery(cmd_args.file)


def init_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("file",
                        help='Parquet file')

    group = parser.add_mutually_exclusive_group()

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

    cmd_args = parser.parse_args()

    return cmd_args


if __name__ == '__main__':
    args = init_args()
    main(args, skip=True)
