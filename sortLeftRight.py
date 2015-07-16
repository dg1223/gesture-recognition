# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:11:32 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
from natsort import natsorted

source = 'C:\\Users\\Shamir\\Desktop\\denoised3(final)\\'   # source folder
filelist = os.listdir(source)
filelist = natsorted(filelist)                              # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Left)\\'        # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Right)\\'       # gestures performed only with the right hand go here
fileformat = '.csv'
backslash = '\\'

for eachfile in range(len(filelist)): # len(filelist)

    csvfile = source + filelist[eachfile]   # full filepath
    file = pandas.read_csv(csvfile, header = None)
    file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns
    num_rows = len(file)                                                            # number of rows in the dataset
    num_columns = len(file.values[0])                                               # number of columns after preprocessing
