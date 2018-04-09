import argparse

import pyarrow.parquet as pq


def summery(parquet_file):
    r = pq.ParquetFile(parquet_file)
    print("\n # Metadata \n", r.metadata)
    print("\n # Schema \n", r.schema)
    return {"metadata": r.metadata, "schema": r.schema}


def get_top(parquet_file, n):
    r = pq.read_table(parquet_file)
    print(r.to_pandas().head(n))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("file",
                        help='Parquet file')
    parser.add_argument("-t", "--top",
                        type=int,
                        default=10,
                        help="Get top N rows from file",
                        )

    args = parser.parse_args()

    if args.top:
        get_top(args.file, args.top)
    else:
        summery(args.file)
