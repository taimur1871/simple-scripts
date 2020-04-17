# create a text file with bit details

import os

#bit_size = input('enter bit size\t')
sr_no = input('enter serial number\t')
bitType= input('enter bit type\t')

import folder_select

with open('bit.txt', 'w') as file1:
    #file1.write(bit_size)
    file1.write(sr_no)
    file1.write(bitType)
