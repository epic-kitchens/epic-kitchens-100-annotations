import os
import sys
import argparse
import pandas as pd
from pathlib import Path


def main(args):
    for path in args.dataframe_paths:
        df = pd.read_pickle(path)
        metadata = {'commit_hash': args.commit_hash, 'version_number': args.version_number}
        df._metadata = metadata
        pd.to_pickle(df, path, protocol=2)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Adds metadata to a pandas dataframe stored in a pickle')
    parser.add_argument('dataframe_paths', type=Path, nargs='+',
            help='Pickle file containing pandas dataframe to add metadata to')
    parser.add_argument('--commit-hash', type=str,
            help='Commit hash metadata to store in pandas dataframe.')
    parser.add_argument('--version-number', type=str,
            help='Version Number metadata to store in pandas dataframe.')

    args = parser.parse_args()
    main(args)
