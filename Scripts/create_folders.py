#create new folders

import os

path = input('Enter folder path\n')

while(os.path.isdir(path) != True):
    path = input('Invalid folder path, please reenter\n')

os.chdir(path)
num_folders = input('Enter number of folders to create\n')
name_folder = input('Enter folder name\n')

for i in range (int(num_folders)):
    os.mkdir(name_folder + ' ' + str(i+1))
