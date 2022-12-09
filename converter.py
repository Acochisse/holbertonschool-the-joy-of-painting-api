#!/usr/bin/env python3
"""
This module modifies a plaintext file into a csv by removing quotes and parentheses and adding commas between the name of the episdoe and the date

"""

import argparse

import sys

def converter():
    """Opens a plaintext file and modifies it into a csv file, removing quotes and parentheses and adding commas between the name of the episode and the date using text replace"""

    with open('src_files/JOP-episodes', 'r') as f:
        with open('src_files/JOP-episodes.csv', 'w') as f2:
            for line in f:
                line = line.replace('(', ',')
                line = line.replace(')', '')
                line = line.replace('"', '')
                f2.write(line)

if __name__ == '__main__':
    converter()
