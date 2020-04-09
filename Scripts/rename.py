#CHANGE NAME

import os


import folder_select

#folder = input('enter the folder with files to be renamed\n')
pictype = input('enter B for Blade, G for Gauge, C for Cutter\n')

#os.chdir(folder)
filenames = os.listdir()
i = 1   #to start file name at 1

for files in filenames:
    if pictype == 'Folder':
        os.rename(files, pictype+str(i))
    else:
        os.rename(files, pictype+str(i)+'.jpg')
    i+=1
