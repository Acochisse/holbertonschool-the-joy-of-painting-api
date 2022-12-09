#!/usr/bin/python3
"""This module extracts raw data from plaintext files and inserts it into a database"""

import pandas as pd


def extract_data():
    """Extracts data from plaintext files and inserts it into a database"""
    # Read in data from plaintext files
    df = pd.read_csv('src_files/JOP-episodes.csv', header=None, usecols=[0,1,2], names = ['Episode_title', 'Month and Day', 'Year'])

    print(df)


if __name__ == '__main__':
    extract_data()
