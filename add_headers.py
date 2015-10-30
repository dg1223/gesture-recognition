# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 20:58:30 2015

@author: Shamir
"""

## BIG BUG!!! : It deletes the 1st row!!! Please swap left and right in 'sortLeftRight' | solution: insert empty header row 1st



import pandas
import os
import numpy as np

sourcePath = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\CSV Files\\P11\\'
fileformat = '.csv'
backslash = '\\'
header = np.array(['qr','qx','qy','qz','time'])

for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures len(os.listdir(sourcePath))
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard 
    print gesture
    filelist = os.listdir(sourcePath + gesture)
          
    for k in range(len(os.listdir(sourcePath + gesture))):    
        File = filelist[k]          # desired csv file in the folder 
        print 'k = ', k, 'file = ', File
        csvfile = sourcePath + gesture + backslash + File   # full filepath
        readFile = pandas.read_csv(csvfile)
        number_of_columns = len(readFile.values[0])        
        #print number_of_columns
        Header = np.tile(header, number_of_columns/5)
        #readFile.insert(0, )
        
        # this calculation does not yield 100% correct (bug free) result >> P3 (Uppercut): had a few 'nan' values in the header columns > corrected manually       
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
        readFile.to_csv(sourcePath + gesture + backslash + File[0:-4] + fileformat, header = Header, index = None)
    
    
    