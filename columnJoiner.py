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

source_left = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Left\\'                   # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Right\\'                 # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Left_combined\\'   # qr, qx, qy, qz combined
destination_right =  'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Right_combined\\' 
fileformat = '.csv'    


def Join(sourcePath, destinationPath): 
       
    count = 1
    output_list = []
    filelist = os.listdir(sourcePath)
    filelist = natsorted(filelist)
    for i in range(0, len(filelist), 4):
        #print 'file = ', i
        firstFile  = pandas.read_csv(sourcePath + filelist[i],     header = None) 
        secondFile = pandas.read_csv(sourcePath + filelist[i + 1], header = None)        
        thirdFile  = pandas.read_csv(sourcePath + filelist[i + 2], header = None)
        fourthFile = pandas.read_csv(sourcePath + filelist[i + 3], header = None)
        print 'lengths = ', len(firstFile.values[0]), len(secondFile.values[0]), len(thirdFile.values[0]), len(fourthFile.values[0])
        
        # Force largest array to drop one column to become equal with others (assuming dropping one columns should suffice)
        lengths = [len(firstFile.values[0]), len(secondFile.values[0]), len(thirdFile.values[0]), len(fourthFile.values[0])]
        max_len_index = lengths.index(max(lengths))
        if max_len_index == 0:
            firstFile = firstFile.drop(range(len(firstFile.values[0]) - 1, len(firstFile.values[0])), axis = 1)
        elif max_len_index == 1:
            secondFile = secondFile.drop(range(len(secondFile.values[0]) - 1, len(secondFile.values[0])), axis = 1)
        elif max_len_index == 2:
            thirdFile = thirdFile.drop(range(len(thirdFile.values[0]) - 1, len(thirdFile.values[0])), axis = 1)
        elif max_len_index == 1:
            fourthFile = fourthFile.drop(range(len(fourthFile.values[0]) - 1, len(fourthFile.values[0])), axis = 1)
        
        
        num_rows =    len(firstFile)   
        num_columns = len(firstFile.values[0])
        #print 'rows, col = ', num_rows, num_columns
        for j in range(num_rows):
            #print "j = ", j
            for k in range(num_columns):                
                #print 'file = ', i, "row = ", j, "col = ", k
                output_list.append(firstFile.loc [j, k])
                output_list.append(secondFile.loc[j, k])
                output_list.append(thirdFile.loc [j, k])
                output_list.append(fourthFile.loc[j, k])

            if j == 0:    
                output_array = np.asarray(output_list)
                #print 'list_shape = ', np.shape(output_list)
                output_list = []
            else:
                #print 'arr_shape = ', np.shape(output_array), 'list_shape = ', np.shape(output_list)
                output_array = np.vstack((output_array, output_list))
                output_list = []
        
        output_array = DataFrame(output_array)        
        output_array.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)
        count += 1
        #print "i = ", i, " done"
        
Join(source_left, destination_left)
Join(source_right, destination_right)

print time.clock() - start, 'seconds taken to execute the program' 