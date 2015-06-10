# -*- coding: utf-8 -*-
"""
Created on Thu Jun 01 01:11:52 2015

@author: Shamir
"""

import pandas
import numpy as np
import os

gesture_path = 'C:\\Users\\Shamir\\Desktop\\Grad\\Gesture Stuff\\Data_Multisensor\\'    # use input() to make it interactive
destination =  'C:\\Users\\Shamir\\Desktop\\broken down files\\'
fileformat = '.csv'
backslash = '\\'

count = 1
for i in range(len(os.listdir(gesture_path))):                                          # we have 6 files corresponding to 6 gestures
    gesture = os.listdir(gesture_path)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
    
    for j in range(len(os.listdir(gesture_path + gesture))):                            # we have 3 files corresponding to 3 datasets (train, cross-validation, test)
        dataset = os.listdir(gesture_path + gesture)[j]                                 # Train, Cross Validation, Test
        
        for k in range(len(os.listdir(gesture_path + gesture + backslash + dataset))):  # we have 5 sensors (15,16,17,18,19) 
            file = os.listdir(gesture_path + gesture + backslash + dataset)[k]          # desired csv file in the folder           
            csvfile = gesture_path + gesture + backslash + dataset + backslash + file   # full filepath
            print csvfile
            readFile = pandas.read_csv(csvfile, header = None)                          # read csv file
            
            qr = readFile.loc[:, range(0, readFile.shape[1], 5)]                            # qr columns only
            qr.to_csv(destination + str(count) + fileformat, header = False, index = False)
            count += 1
            
            qx = readFile.loc[:, range(1, readFile.shape[1], 5)]                            # qx columns only
            qx.to_csv(destination + str(count) + fileformat, header = False, index = False)
            count += 1
            
            qy = readFile.loc[:, range(2, readFile.shape[1], 5)]                            # qy columns only  
            qy.to_csv(destination + str(count) + fileformat, header = False, index = False)
            count += 1
            
            qz = readFile.loc[:, range(3, readFile.shape[1], 5)]                            # qz columns only
            qz.to_csv(destination + str(count) + fileformat, header = False, index = False)
            count += 1