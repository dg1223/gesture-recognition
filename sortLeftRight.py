# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 16:11:32 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
from natsort import natsorted
from pandas import DataFrame

# function to copy headers into destination arrays
def copyHeaders(source):
    dest_list = []
    dest_list.append(source.tolist())
    dest_array = np.asarray(dest_list)
    return dest_array

source = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Broken down files\\P8\\'                       # source folder
filelist = os.listdir(source)
filelist = natsorted(filelist)                                                                           # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Left\\'         # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Right\\'        # gestures performed only with the right hand go here
fileformat = '.csv'
count = 1

for eachfile in range(len(filelist)):               # len(filelist)

    csvfile = source + filelist[eachfile]                                       # full filepath
    file = pandas.read_csv(csvfile, header = None)
    file.values[1:] = file.values[1:].astype(float)                             # convert all strings to floats; ignore header columns
    num_rows = len(file)                                                        # number of rows in the dataset
    
    # identical headers for both types of gestures
    left  = copyHeaders(file.values[0])                                         
    right = copyHeaders(file.values[0])                                         
    
    
    for i in range(1, num_rows):                    # 1, num_rows
        if i % 2 == 1:                                                          # if row is odd (zero indexed), it is a right hand gesture 
            right = np.vstack((right, file.values[i]))      
        else:                                                                   # if row is even (zero indexed), it is a left hand gesture
            left  = np.vstack((left, file.values[i]))
    
    # convert to pandas dataframe in order to write data in a csv file
    right = DataFrame(right)
    left  = DataFrame(left)
    
    # write seperate csv files for individual hands
    right.to_csv(destination_right + str(count) + fileformat, header = False, index = False)
    left.to_csv(destination_left + str(count) + fileformat, header = False, index = False)
    
    count += 1                                                                  # increment counter for next filename
    right, left = [], []                                                        # empty array for next iteration
        