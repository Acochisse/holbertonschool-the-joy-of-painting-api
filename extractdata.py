#!/usr/bin/python3
"""This module extracts raw data from plaintext files and inserts it into a database"""

import pandas as pd
import sqlite3
import json
import os
import sys
import time
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


color_range = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#rewrite color_array in the same order modified with capitol first letter and no underscores example 'Apple Frame'
color_array = ['Black Gesso', 'Bright Red', 'Burnt Umber', 'Cadmium Yellow',
        'Dark Sirius', 'Indian Red', 'Indian Yellow', 'Liquid Black', 'Liquid Clear',
        'Midnight Black', 'Phthalo Blue', 'Phthalo Green', 'Prussian Blue', 'Sap Green',
        'Titanium White', 'Van Dyke Brown', 'Yellow Ochre', 'Alizarin Crimson']

subjects_array = ['Apple Frame','Aurora Borealis','Barn','Beach','Boat','Bridge','Building','Bushes',
        'Cabin','Cactus','Circle Frame','Cirrus','Cliff','Clouds','Conifer','Cumulus','Deciduous','Diane Andre',
        'Dock','Double Oval Frame','Farm','Fence','Fire','Florida Frame','Flowers','Fog','Framed',
        'Grass','Guest','Half Circle Frame','Half Oval Frame','Hills','Lake','Lakes','Lighthouse',
        'Mill','Moon','Mountain','Mountains','Night','Ocean','Oval Frame','Palm Trees','Path','Person',
        'Portrait','Rectangle 3D Frame','Rectangular Frame','River','Rocks','Seashell Frame','Snow','Snowy Mountain',
        'Split Frame','Steve Ross','Structure','Sun','Tomb Frame','Tree','Trees','Triple Frame','Waterfall','Waves',
        'Windmill','Window Frame','Winter','Wood Framed']


color_arrlen = len(color_array)
color_rangelen = len(color_range)
subjects_range = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
                    31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68]
sub_arraylen = len(subjects_array)
sub_rangelen = len(subjects_range)
print (sub_arraylen,sub_rangelen)
print (color_arrlen,color_rangelen)


def extract_data():
    """Extracts data from the file src_files/JOP-sm and inserts it into a dataframe"""
    df = pd.read_csv('src_files/JOP-episodes.csv', header=None, usecols=[0,1,2], names = ['Episode_title', 'Month and Day', 'Year'])
    df.insert(2, 'Day', df['Month and Day'].str.split(' ').str[1])
    df.insert(2, 'Month', df['Month and Day'].str.split(' ').str[0])
    df.pop('Month and Day')
    print (df)
    df2 = pd.read_csv('src_files/JOP-colors', header=None, skiprows=1, usecols=color_range, names = color_array)
    df3 = pd.read_csv('src_files/JOP-sm', header=None, skiprows=1, usecols=subjects_range, names = subjects_array)
    conn = sqlite3.connect('Joy_of_Painting.db')
    c = conn.cursor()
    """Combines the dataframes into one dataframe"""
    df_final = pd.concat([df,df2,df3], axis=1)
    df_final.to_sql('Joy_of_Painting.db', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    
    extract_data()