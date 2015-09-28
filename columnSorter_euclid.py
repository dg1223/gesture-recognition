# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:38:01 2015

@author: Shamir
"""

import pandas
import os
import time
from natsort import natsorted

start = time.clock()

source_left = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Left\\'                    # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Right\\'                  # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean_components\\P1\\Left\\'  # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean_components\\P1\\Right\\' # gestures performed only with the right hand go here
fileformat = '.csv'


def separateEuclidAngles(sourcePath, destinationPath):
    
    count = 1
    filelist = os.listdir(sourcePath)
    filelist = natsorted(filelist)
    for i in range(len(filelist)):
        csvfile  = pandas.read_csv(sourcePath + filelist[i], header = None)
        
        alpha = csvfile.loc[:, range(0, csvfile.shape[1], 3)]                                   # alpha columns only
        alpha.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        
        beta = csvfile.loc[:, range(1, csvfile.shape[1], 3)]                                    # beta columns only
        beta.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        
        gamma = csvfile.loc[:, range(2, csvfile.shape[1], 3)]                                   # gamma columns only
        gamma.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        
separateEuclidAngles(source_left, destination_left)
separateEuclidAngles(source_right, destination_right)
        
print time.clock() - start, 'seconds taken to execute the program' 