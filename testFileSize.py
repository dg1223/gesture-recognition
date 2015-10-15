# -*- coding: utf-8 -*-
"""
Created on Fri Oct 09 20:18:43 2015

@author: Shamir
"""

import pandas
import os
from natsort import natsorted

sourceLeft  = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P3\\Left\\'
sourceRight = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P3\\Right\\'
fileformat  = '.csv'
backslash   = '\\'

def printLength(source):
    for i in range(len(os.listdir(source))):
        filename = natsorted(os.listdir(source))[i]
        csvfile = sourceRight + filename
        readFile = pandas.read_csv(csvfile, header = None)
        
        print 'filename = ', csvfile[-7:], ', length = ', len(readFile.values)
        

#print 'Left Sorted'
#printLength(sourceLeft)
print 'Right Sorted'
printLength(sourceRight)