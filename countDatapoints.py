# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:35:25 2015

@author: Shamir
"""

import pandas
import os
from natsort import natsorted
from math import isnan

source_left  = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Left\\'                
source_right = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Right\\'               
fileformat        = '.csv'

def CountData(sourcePath):
    
    """
    This function counts the total number of datapoints contained in an entire folder
    
    input parameter : sourcePath; it takes the path of the directory where the files are stored for processing.
    
    """
    count = 0    
    filelist    = os.listdir(sourcePath)                                        # list all the files in the folder
    filelist    = natsorted(filelist)                                           # naturally sort the file list; this fixes the problem of having improper file order in the list
    
    for file in range(len(filelist)):
        csvfile            = pandas.read_csv(sourcePath + filelist[file], header = None)    # read csv file
        csvfile.values[1:] = csvfile.values[1:].astype(float)                   # convert all strings to floats; ignore header columns 
        num_rows           = len(csvfile)                                       # number of rows in the file
        num_columns        = len(csvfile.values[0])                             # number of columns in the file
        
        for i in range(1, num_rows):
            for j in range(0, num_columns):
                
                datapoint = csvfile.values[i,j]
                
                if isnan(datapoint) == True:
                    continue
                else:
                    count += 1
    return count

totalDatapoints = 0
datapoints = CountData(source_left)
print 'datapoints_left = ', datapoints
totalDatapoints += datapoints
datapoints = CountData(source_right)
print 'datapoints_right = ', datapoints
totalDatapoints += datapoints

print 'total number of datapoints  = ', totalDatapoints
print 'total number of coordinates = ', totalDatapoints/3.0

        
        
        
        
        