# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 20:58:30 2015

@author: Shamir
"""

import pandas
import os
import numpy as np

sourcePath = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\CSV Files\\P6\\'
fileformat = '.csv'
backslash = '\\'
header = np.array(['qr','qx','qy','qz','time'])

for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures len(os.listdir(sourcePath))
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard 
    print gesture
    filelist = os.listdir(sourcePath + gesture)
    
    for k in range(len(os.listdir(sourcePath + gesture))):    
        file = filelist[k]          # desired csv file in the folder 
        print 'k = ', k, 'file = ', file
        csvfile = sourcePath + gesture + backslash + file   # full filepath
        readFile = pandas.read_csv(csvfile)
        number_of_columns = len(readFile.values[0])        
        #print number_of_columns
        Header = np.tile(header, number_of_columns/5)
        if number_of_columns % 5 == 1:
            Header = Header.tolist()
            Header.append('qr')
            Header = np.asarray(Header)
        elif number_of_columns % 5 == 2:
            Header = Header.tolist()
            Header.append('qr', 'qx')
            Header = np.asarray(Header)
        elif number_of_columns % 5 == 3:
            Header = Header.tolist()
            Header.append('qr', 'qx', 'qy')
            Header = np.asarray(Header)
        elif number_of_columns % 5 == 4:
            Header = Header.tolist()
            Header.append('qr', 'qx', 'qy', 'qz')
            Header = np.asarray(Header)
        readFile.to_csv(sourcePath + gesture + backslash + file[0:-4] + fileformat, header = Header, index = None)
    
    
    