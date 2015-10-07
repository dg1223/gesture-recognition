# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:52:59 2015

@author: Shamir
"""

import pandas
import os

gesture_path = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\CSV Files\\P6\\'
destination = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Broken down files\\P6\\'
fileformat = '.csv'
backslash = '\\'

count = 1
for i in range(len(os.listdir(gesture_path))):                                          # we have 6 files corresponding to 6 gestures len(os.listdir(gesture_path))
    gesture = os.listdir(gesture_path)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard 
            
    for k in range(len(os.listdir(gesture_path + gesture))):    
        file = os.listdir(gesture_path + gesture)[k]          # desired csv file in the folder           
        csvfile = gesture_path + gesture + backslash + file   # full filepath
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