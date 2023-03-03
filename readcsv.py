# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:32:15 2021
from https://realpython.com/python-csv/
@author: Kerri-Ann Norton
"""

import csv


def load_data(file_name):
    with open(file_name, newline='') as csvfile:
        fishreader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        weights = []
        for row in fishreader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} weighs {row[1]} and is {row[2]}.')
                weights.append(int(row[1]))
                line_count += 1
        print(f'Processed {line_count} lines.')
        return weights
