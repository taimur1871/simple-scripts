"""
see if the file list is passed to the script
"""

import os, csv

# file path
file_path = '/home/taimur/Documents/Python Projects/Test Argparse/test1.txt'

# read csv file list
file_list = []

file_name = open(file_path)

csv_file = csv.reader(file_name, delimiter=',')
for i in csv_file:
    file_list.append(i)

for j in file_list:
    print(j[0])
