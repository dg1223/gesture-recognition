# -*- coding: utf-8 -*-
"""
Created on Fri Sep 04 14:16:00 2015

@author: Shamir
"""

import pandas
import os
from natsort import natsorted
from math import isnan
from pandas import DataFrame

source_left = 'C:\\Users\\Shamir\\Desktop\\Euclidean\\Left\\'                    # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Euclidean\\Right\\'                  # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Euclidean\\Left_NoMissing\\'  # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Euclidean\\Right__NoMissing\\' # gestures performed only with the right hand go here
fileformat = '.csv'

def ReplaceNaN(sourcePath, destinationPath):
    
    count = 1
    filelist = os.listdir(sourcePath)
    filelist = natsorted(filelist)
    
    for i in range(len(filelist)):
        csvfile  = pandas.read_csv(sourcePath + filelist[i], header = None)
        csvfile.values[1:] = csvfile.values[1:].astype(float)                   # convert all strings to floats; ignore header columns 
        num_rows           = len(csvfile)                                       # number of rows in the file
        num_columns        = len(csvfile.values[0])
        
        # loop for conversion to Euclidean angles
        for j in range(1, num_rows):
            for k in range(1, num_columns, 3):                                  # we only need to check columns columns with beta values i.e. every 3rd column starting from the 2nd (1,4,7,10...)
            
                Beta = csvfile.values[j,k]
                if k > 1 and isnan(Beta) == True:
                    csvfile.values[j,k] = csvfile.values[j, k-3]
                elif k == 1 and isnan(Beta) == True:
                    
                    
                
        csvfile = DataFrame(csvfile)
        csvfile.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        
ReplaceNaN(source_left, destination_left)
ReplaceNaN(source_right, destination_right)
                    
        