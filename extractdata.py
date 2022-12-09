#!usr/bin/python3
"""This module extracts raw data from plaintext files and inserts it into a database"""

import pandas as pd


def extract_data():
    """Extracts data from plaintext files and inserts it into a database"""
    # Read in data from plaintext files
    df = pd.read_csv('src_files/-episodes', sep='()', header=None)
    df.columns = ['Episode_title', 'Air date']

    print(df)