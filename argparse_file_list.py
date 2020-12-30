"""
see if the file list is passed to the script
"""

import os, argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument('--file-list', help='list of files to process')

#parser.add_argument('--file-folder', help='folder containing files')

args = parser.parse_args()

# ----------------------------------------------------------------------------

# read csv file list
def read_file(filename):
    file_list = []

    csv_temp = open(filename)
    
    csv_file = csv.reader(csv_temp, delimiter=',')
    
    for i in csv_file:
        #file_list.append(os.path.join(filename, i))
        file_list.append(i[0])

    return file_list

# read list of files from dir
def read_dir(foldername):
    return os.listdir(foldername)

# check if the argument passed is file or folder
if os.path.isfile(args.file_list) == True:
    file_list = read_file(args.file_list)
else:
    file_list = read_dir(args.file_list)

def add_data(inputfiles):
  # Make a list of all files to be processed
    
  for obj in inputfiles:
    print(obj)

# call add_data function
add_data(file_list)

