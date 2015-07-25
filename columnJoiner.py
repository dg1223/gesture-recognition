# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:17:21 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
import time
from natsort import natsorted
from pandas import DataFrame

start = time.clock()

source_left = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Left\\'                # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Right\\'              # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Left_sorted\\'  # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Right_sorted\\' # gestures performed only with the right hand go here
fileformat = '.csv'    


def Join(sourcePath, destinationPath): 
       
    count = 1
    output_list = []
    filelist = os.listdir(sourcePath)
    filelist = natsorted(filelist)
    for i in range(0, len(filelist), 4):
        firstFile  = pandas.read_csv(sourcePath + filelist[i],     header = None) 
        secondFile = pandas.read_csv(sourcePath + filelist[i + 1], header = None)
        thirdFile  = pandas.read_csv(sourcePath + filelist[i + 2], header = None)
        fourthFile = pandas.read_csv(sourcePath + filelist[i + 3], header = None)
        #print "i = ", i, " read"
        num_rows =    len(firstFile)   
        num_columns = len(firstFile.values[0])
        for j in range(num_rows):
            #print "j = ", j
            for k in range(num_columns):
                output_list.append(firstFile.loc [j, k])
                output_list.append(secondFile.loc[j, k])
                #print "j = ", j, "k = ", k
                output_list.append(thirdFile.loc [j, k])
                output_list.append(fourthFile.loc[j, k])
            if j == 0:    
                output_array = np.asarray(output_list)
                output_list = []
            else:
                output_array = np.vstack((output_array, output_list))
                output_list = []
        
        output_array = DataFrame(output_array)        
        output_array.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        print "i = ", i, " done"
        
Join(source_left, destination_left)
Join(source_right, destination_right)

print time.clock() - start, 'seconds taken to execute the program' 