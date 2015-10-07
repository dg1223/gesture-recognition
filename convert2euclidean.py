# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:28:29 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
import time
from natsort import natsorted
from pandas import DataFrame

start = time.clock()                                                            # start counting time (optional)

source_left       = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Left_combined\\'  # source folder
source_right      = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P8\\Right_combined\\' # naturally sort the file list
destination_left  = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P8\\Left Sorted\\'                
destination_right = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P8\\Right Sorted\\'               
fileformat        = '.csv'

def Convert2Euclidean(sourcePath, destinationPath):

    """
    This function converts Quaterinons to Euler angles and saves it in a CSV file.
    
    input parameter : sourcePath;      it takes the path of the directory where the files are stored for processing.
    output parameter: destinationPath; it takes the path of the directory where the new data would be stored in corresponding files. The files are numbered from 1 to n, n being the total number of files.
    
    """

    count_errors = 0
    count       = 1                                                             # start count for file numbers
    output_list = []                                                            # temporary storage list before passing data to an array
    filelist    = os.listdir(sourcePath)                                        # list all the files in the folder
    filelist    = natsorted(filelist)                                           # naturally sort the file list; this fixes the problem of having improper file order in the list
    
    for file in range(len(filelist)):       # len(filelist)
        
        #print "reading file # ", file       
        csvfile            = pandas.read_csv(sourcePath + filelist[file], header = None)    # read csv file
        csvfile.values[1:] = csvfile.values[1:].astype(float)                   # convert all strings to floats; ignore header columns 
        num_rows           = len(csvfile)                                       # number of rows in the file
        num_columns        = len(csvfile.values[0])                             # number of columns in the file
        
        # Creater header row
        for i in range(0, num_columns, 4):
            output_list.append('alpha')
            output_list.append('beta')
            output_list.append('gamma')
        
        #print "shape of 1st output_list = ", np.shape(output_list)
        output_array = np.asarray(output_list)                                  # initialize the storage array with headers
        output_list  = []                                                       # empty temporary list
        #print "shape of output_array = ", np.shape(output_array)
        
        # loop for conversion to Euclidean angles
        for i in range(1, num_rows):
            for j in range(0, num_columns, 4):                                  # we need to take 4 columns in each iteration; 1 quaternion = 4 elements
                
                # precalculate indexes of the vector elements of each quaternion for faster memory operation
                secondIndex = j + 1
                thirdIndex  = j + 2
                fourthIndex = j + 3
                
                qr = float(csvfile.values[i, j])
                qx = float(csvfile.values[i, secondIndex])
                qy = float(csvfile.values[i, thirdIndex])
                qz = float(csvfile.values[i, fourthIndex])
                
                                
                # Calculate the Euler Angles in degrees (multiplying the radian terms with 180/pi)
                #print "reading i, j = ", i, j
                try:
                    Alpha = np.arctan ((2*(qr*qx + qy*qz)) / (1 - 2*(np.square(qx) + np.square(qy)))) * 180/np.pi    
                except:
                    print 'file, row, col = ', file, i, j
                    print qr, qx, qy, qz
                ## Major bug, possibly due to noise. This test value, given that the condition becomes true, should not be used for actual analysis. Instead, please filter the noise through the modified filter.
                test = 2*(qr*qy - qx*qz)                
                if test < -1.0:
                    count_errors += 1
                    #test = -1.0
                elif test > 1.0:
                    count_errors += 1
                    #test = 1.0
                    
                Beta  = np.arcsin (test)                                                          * 180/np.pi
                
                #print Beta                    
                #if isnan(Beta) == True:
                    #print "qr = ", qr
                    #print "qx = ", qx
                    #print "qy = ", qy
                    #print "qz = ", qz
                    #break
                
                Gamma = np.arctan ((2*(qr*qz + qx*qy)) / (1 - 2*(np.square(qy) + np.square(qz)))) * 180/np.pi
                
                # save the calculated values in the temporary storage
                output_list.append(Alpha)
                output_list.append(Beta)
                output_list.append(Gamma)
                
                #except ValueError:                 # if we encounter NaN values
                 #   pass
            
            #print "shape of 2nd output_list = ", np.shape(output_list)
            output_array = np.vstack((output_array, output_list))               # insert each converted row into the storage array
            output_list  = []                                                   # empty temporary list for next iteration
        
        output_array = DataFrame(output_array)                                  # convert complete array into a Pandas Dataframe 
        output_array.to_csv(destinationPath + str(count) + fileformat, header = False, index = False)   # write the dataframe to a csv file
        count += 1                                                              # increment file counter
    print 'bad Beta values = ', count_errors    

Convert2Euclidean(source_left, destination_left)
Convert2Euclidean(source_right, destination_right)

print time.clock() - start, 'seconds taken to execute the program' 
