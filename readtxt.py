# -*- coding: utf-8 -*-
"""
Created on Mon Oct 05 20:04:03 2015

@author: Shamir
"""

import pandas
import os

sourcePath = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\CSV Files\\P8\\'
fileformat = '.csv'
backslash = '\\'

for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures 
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard 
    print gesture
    filelist = os.listdir(sourcePath + gesture)
            
    for k in range(len(os.listdir(sourcePath + gesture))):    
        file = filelist[k]          # desired csv file in the folder 
        print 'k = ', k, 'file = ', file
        csvfile = sourcePath + gesture + backslash + file   # full filepath
        try:
            readFile = pandas.read_csv(csvfile, sep = ' ')
            readFile.to_csv(sourcePath + gesture + backslash + file[0:-4] + fileformat, header = None, index = None)
        except pandas.parser.CParserError as e:    
            columns_to_consider = int(e.message[-5:])
            if columns_to_consider % 5 != 0:
                columns_to_consider -=  columns_to_consider % 5
            readFile = pandas.read_csv(csvfile, sep = ' ', names = range(0, columns_to_consider))
            readFile.to_csv(sourcePath + gesture + backslash + file[0:-4] + fileformat, header = None, index = None)