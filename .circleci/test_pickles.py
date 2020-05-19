import os
import sys
import argparse
import pandas as pd
from pathlib import Path


def test_files(pkl_paths, csv_paths, commit_hash, version_number):
    for pkl_path, csv_path in zip(pkl_paths, csv_paths):
        csv = pd.read_csv(csv_path)
        df = pd.read_pickle(pkl_path)
        assert_equal(commit_hash, df._metadata['commit_hash'])
        assert_equal(version_number, df._metadata['version_number'])
        assert_equal(len(df), len(csv))
        csv_ids = set(csv[csv.columns[0]])
        df_ids = set(df.index)
        assert csv_ids == df_ids, get_csv_error_message(pkl_path, csv_path, csv_ids, df_ids)

def get_csv_error_message(csv_path, pkl_path, csv_ids, df_ids):
    in_csv_not_in_df = csv_ids - df_ids
    in_df_not_in_csv = df_ids - csv_ids
    message = ""
    if len(in_csv_not_in_df) > 0:
        message += f"IDs in CSV ({csv_path}) but not present in DataFrame ({pkl_path}):\n"
        message += missing_set_message(in_csv_not_in_df)
    if len(in_df_not_in_csv) > 0:
        if len(message) > 0:
            message += "\n"
        message += f"IDs in DataFrame ({pkl_path}) but not present in CSV ({csv_path}):\n"
        message += missing_set_message(in_df_not_in_csv)
    return message


def missing_set_message(set_, max_items=50):
    def elems_to_str(elems):
        return ", ".join(map(str, elems))

    if len(set_) <= max_items:
        return elems_to_str(set_) + "\n"

    as_list = list(set_)
    return "{}, ..., {}".format(
        elems_to_str(as_list[:max_items//2]),
        elems_to_str(as_list[-max_items//2:])
    ) + "\n"


def assert_equal(expected, actual):
    assert expected == actual, "Expected {} but was {}".format(expected, actual)


def main(args):
    pkl_paths = args.pickle_paths
    csv_paths = [pkl_path.with_suffix('.csv') for pkl_path in pkl_paths]
    test_files(pkl_paths, csv_paths, args.commit_hash, args.version_number)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tests pickles can be read and the metadata exists')
    parser.add_argument('pickle_paths', type=Path, nargs='+',
            help='Pickle file containing pandas dataframe to add metadata to')
    parser.add_argument('--commit-hash', type=str,
            help='Commit hash metadata to store in pandas dataframe.')
    parser.add_argument('--version-number', type=str,
            help='Version Number metadata to store in pandas dataframe.')

    args = parser.parse_args()
    main(args)
