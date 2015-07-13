# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 23:31:44 2015

@author: Shamir
"""
import pandas
import os
import time
#import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import euclidean
from natsort import natsorted

start = time.clock()

# function for Linear Interpolation
def linearInterpolation(prev_datapoint, target_datapoint, next_datapoint):
    denominator = next_datapoint - prev_datapoint
    numerator = ((target_datapoint - prev_datapoint) * (file.values[i, next_datapoint] - file.values[i, prev_datapoint]))
    interpolated_value = (numerator/denominator) + file.values[i, prev_datapoint]    
    return interpolated_value

# function for derivative filtering    
def firstDerivative(prev, curr, nexT):
    try:
        derivative = (abs(prev - curr) + abs(curr - nexT)) / abs(prev - nexT)        
        return derivative
    except ZeroDivisionError:   # as detail:
        if abs(prev - curr) == abs(nexT - curr):
            error = 1
            return error
        #print 'Two identical datapoints:', detail
        pass

source = 'C:\\Users\\Shamir\\Desktop\\broken down files\\'   # broken down files
filelist = os.listdir(source)
filelist = natsorted(filelist)                               # naturally sort the file list
destination =  'C:\\Users\\Shamir\\Desktop\\denoised3(final)\\'
fileformat = '.csv'
backslash = '\\'
count = 1

## Algorithm for filtering noisy peaks
for eachfile in range(len(filelist)): # len(filelist)
    
    # fileHandler (can become a different class!)
    csvfile = source + filelist[eachfile]   # full filepath
    file = pandas.read_csv(csvfile, header = None)
    file = file.dropna(axis = 1)                                                    # reject every column that contains at least one NaN value (we lose at least one instance of gesture) - use only for unprocessed datasets
    #file = file.drop(range(0,40), axis = 1)                                         # delete 1st 40 points          
    file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns 
    
    #plt.plot(file.values[32, 0:5])
    
    num_rows = len(file)                                                            # number of rows in the dataset
    num_columns = len(file.values[0])                                               # number of columns after preprocessing
    column_limit = num_columns - 1                                                  # boundary condition for iterating through columns
    thresh = 0.12                                                                   # threshold to find peaks (noisy values based-on euclidean distance)
     
    # start denoising every dataset               
    for i in range(1, num_rows): # 1, num_rows
        index = 1                                                               # index of current datapoint       
                                                          
        for j in range(num_columns):
            if index == num_columns - 1:
                #print ("error: index == num_columns - 1")
                break        
            else:
                # prev_point (1), index (2), next_point (3), secNext_point (4), thirdNext_point (5), fourthNext_point (6), window_bound (7)
                prev_point       = index - 1                                        
                next_point       = index + 1
                secNext_point    = index + 2
                thirdNext_point  = index + 3
                fourthNext_point = index + 4
                window_bound     = index + 5
                
                ## if boundary condition is False and euclidean distance is greater than threshold, perform Linear Interpolation. Check for consecutive, noisy datapoints (window size = 6)
                ## and perform L.I. on each noisy value with the previous and next clean datapoints.
                if (index < (num_columns - 1)) and (euclidean(file.values[i, index], file.values[i, prev_point]) <= thresh):
                    #print ("0th condition")
                    index += 1
                    
                elif (index < (num_columns - 1)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
                and euclidean(file.values[i, next_point], file.values[i, prev_point]) <= thresh:
                    #print ("1st condition")
                    file.values[i, index] = linearInterpolation(prev_point, index, next_point)
                    index += 2
            
                elif (index < (num_columns - 3)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) <= thresh):
                    file.values[i, index] = linearInterpolation(prev_point, index, secNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, secNext_point)
                    #print ("2nd condition")
                    index += 3
                    
                elif (index < (num_columns - 4)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, thirdNext_point], file.values[i, prev_point]) <= thresh):
                    file.values[i, index] = linearInterpolation(prev_point, index, thirdNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, thirdNext_point)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, thirdNext_point)
                    #print ("3rd condition")
                    index += 4
                    
                elif (index < (num_columns - 5)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, thirdNext_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, window_bound], file.values[i, prev_point]) <= thresh):
                    file.values[i, index] = linearInterpolation(prev_point, index, window_bound)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, window_bound)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, window_bound)
                    file.values[i, thirdNext_point] = linearInterpolation(prev_point, thirdNext_point, window_bound)
                    #print ("4th condition")
                    index += 5
                    
                elif (index < (num_columns - 6)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, thirdNext_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, fourthNext_point], file.values[i, prev_point]) > thresh)\
                and (euclidean(file.values[i, window_bound], file.values[i, prev_point]) <= thresh):
                    file.values[i, index] = linearInterpolation(prev_point, index, window_bound)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, window_bound)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, window_bound)
                    file.values[i, thirdNext_point] = linearInterpolation(prev_point, thirdNext_point, window_bound)
                    file.values[i, fourthNext_point] = linearInterpolation(prev_point, fourthNext_point, window_bound)
                    print ("5th condition")
                    index += 6
                # if there is no noise inside the window, go to next datapoint    
                elif index < num_columns - 1:
                    index += 1
        #print ("prev_point = "), prev_point    
        #print ("index = "), index    
        #print ("next_point = "), next_point
        
    #plt.plot(file.values[32, 0:5])               
    
    ## Derivative filtering
    
    thresh2 = 2.5
    
    for i in range(1, num_rows):#
        index = 1
                
        for j in range(num_columns):
            if index == num_columns - 1:
                #print ("error: index == num_columns - 1")
                break        
            else:
                # prev_point (1), index (2), next_point (3), secNext_point (4), thirdNext_point (5), fourthNext_point (6), window_bound (7)
                prev_point        = index - 1                                        
                next_point        = index + 1
                secNext_point     = index + 2
                thirdNext_point   = index + 3
                fourthNext_point  = index + 4
                fifthNext_point   = index + 5
                sixthNext_point   = index + 6
                seventhNext_point = index + 7
                eigthNext_point   = index + 8
                ninthNext_point   = index + 9
                window_bound      = index + 10
                
                if (index < (num_columns - 1))\
                and (file.values[i, index] - file.values[i, prev_point] == 0):
                    #print ("0th derivative condition")
                    index += 1
                
                elif (index < (num_columns - 1))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point]) == 1\
                and file.values[i, prev_point] == file.values[i, next_point]:
                    file.values[i, index] = linearInterpolation(prev_point, index, next_point)
                    #print ("condition: zreo division error with noise [1] [example: -0.089, 0.024, -0.089]")
                    index += 2
                
                elif (index < (num_columns - 2))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point]) == 1\
                and file.values[i, prev_point] == file.values[i, secNext_point]:
                    file.values[i, index] = linearInterpolation(prev_point, index, secNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, secNext_point)
                    #print i, index
                    #print ("condition: zreo division error with noise [2] [example: -0.089, 0.024, 0.024, -0.089]")
                    index += 3
                    
                elif (index < (num_columns - 3))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point]) == 1\
                and file.values[i, prev_point] == file.values[i, thirdNext_point]:
                    file.values[i, index] = linearInterpolation(prev_point, index, thirdNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, thirdNext_point)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, thirdNext_point)
                    #print i, index
                    #print ("condition: zreo division error with noise [3] [example: -0.089, 0.024, 0.024, 0.024, -0.089]")
                    index += 4
                    
                elif (index < (num_columns - 4))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point]) == 1\
                and file.values[i, prev_point] == file.values[i, fourthNext_point]:
                    file.values[i, index] = linearInterpolation(prev_point, index, fourthNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, fourthNext_point)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, fourthNext_point)
                    file.values[i, thirdNext_point] = linearInterpolation(prev_point, thirdNext_point, fourthNext_point)
                    #print i, index
                    #print ("condition: zreo division error with noise [4] [example: -0.089, 0.024, 0.024, 0.024, 0.024, -0.089]")
                    index += 5
                    
                elif (index < (num_columns - 1))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point]) > thresh2:
                    file.values[i, index] = linearInterpolation(prev_point, index, next_point)
                    #print ("first 1st derivative condition")
                    index += 2
                    
                elif (index < (num_columns - 2))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])    <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])  > thresh2:
                    file.values[i, index]      = linearInterpolation(prev_point, index, secNext_point)
                    file.values[i, next_point] = linearInterpolation(prev_point, next_point, secNext_point)
                    #print ("Second 1st derivative condition")
                    index += 2
                    
                elif (index < (num_columns - 3))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])      <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])  > thresh2:
                    #print i, index
                    #print ("third 1st derivative condition")
                    file.values[i, index]         = linearInterpolation(prev_point, index, thirdNext_point)
                    file.values[i, next_point]    = linearInterpolation(prev_point, next_point, thirdNext_point)
                    file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, thirdNext_point)
                    index += 3
                    

                elif (index < (num_columns - 4))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])       <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])    <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point])  > thresh2:
                    #print i, index
                    #print ("fourth 1st derivative condition")
                    file.values[i, index]           = linearInterpolation(prev_point, index, fourthNext_point)
                    file.values[i, next_point]      = linearInterpolation(prev_point, next_point, fourthNext_point)
                    file.values[i, secNext_point]   = linearInterpolation(prev_point, secNext_point, fourthNext_point)
                    file.values[i, thirdNext_point] = linearInterpolation(prev_point, thirdNext_point, fourthNext_point)
                    
                    index += 4
                 
                elif (index < (num_columns - 5))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])       <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])    <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point]) <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])   > thresh2:
                    file.values[i, index]            = linearInterpolation(prev_point, index, fifthNext_point)
                    file.values[i, next_point]       = linearInterpolation(prev_point, next_point, fifthNext_point)
                    file.values[i, secNext_point]    = linearInterpolation(prev_point, secNext_point, fifthNext_point)
                    file.values[i, thirdNext_point]  = linearInterpolation(prev_point, thirdNext_point, fifthNext_point)
                    file.values[i, fourthNext_point] = linearInterpolation(prev_point, fourthNext_point, fifthNext_point)
                    #print i, index
                    #print ("fifth 1st derivative condition")
                    index += 5
                 
                elif (index < (num_columns - 6))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])       <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])    <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point]) <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, sixthNext_point])   > thresh2:
                    file.values[i, index]            = linearInterpolation(prev_point, index, sixthNext_point)
                    file.values[i, next_point]       = linearInterpolation(prev_point, next_point, sixthNext_point)
                    file.values[i, secNext_point]    = linearInterpolation(prev_point, secNext_point, sixthNext_point)
                    file.values[i, thirdNext_point]  = linearInterpolation(prev_point, thirdNext_point, sixthNext_point)
                    file.values[i, fourthNext_point] = linearInterpolation(prev_point, fourthNext_point, sixthNext_point)
                    file.values[i, fifthNext_point]  = linearInterpolation(prev_point, fifthNext_point, sixthNext_point)
                    #print i, index
                    #print ("sixth 1st derivative condition")
                    index += 6
                
                elif (index < (num_columns - 7))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])        <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])     <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, sixthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, seventhNext_point])  > thresh2:
                    file.values[i, index]            = linearInterpolation(prev_point, index, seventhNext_point)
                    file.values[i, next_point]       = linearInterpolation(prev_point, next_point, seventhNext_point)
                    file.values[i, secNext_point]    = linearInterpolation(prev_point, secNext_point, seventhNext_point)
                    file.values[i, thirdNext_point]  = linearInterpolation(prev_point, thirdNext_point, seventhNext_point)
                    file.values[i, fourthNext_point] = linearInterpolation(prev_point, fourthNext_point, seventhNext_point)
                    file.values[i, fifthNext_point]  = linearInterpolation(prev_point, fifthNext_point, seventhNext_point)
                    file.values[i, sixthNext_point]  = linearInterpolation(prev_point, sixthNext_point, seventhNext_point)
                    #print i, index
                    #print ("seventh 1st derivative condition")
                    index += 7
                
                elif (index < (num_columns - 8))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])        <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])     <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, sixthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, seventhNext_point]) <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, eigthNext_point])    > thresh2:
                    file.values[i, index]             = linearInterpolation(prev_point, index, eigthNext_point)
                    file.values[i, next_point]        = linearInterpolation(prev_point, next_point, eigthNext_point)
                    file.values[i, secNext_point]     = linearInterpolation(prev_point, secNext_point, eigthNext_point)
                    file.values[i, thirdNext_point]   = linearInterpolation(prev_point, thirdNext_point, eigthNext_point)
                    file.values[i, fourthNext_point]  = linearInterpolation(prev_point, fourthNext_point, eigthNext_point)
                    file.values[i, fifthNext_point]   = linearInterpolation(prev_point, fifthNext_point, eigthNext_point)
                    file.values[i, sixthNext_point]   = linearInterpolation(prev_point, sixthNext_point, eigthNext_point)
                    file.values[i, seventhNext_point] = linearInterpolation(prev_point, seventhNext_point, eigthNext_point)
                    #print i, index
                    #print ("eigth 1st derivative condition")
                    index += 8
                # inconsistent with the earlier ones    
                elif (index < (num_columns - 9))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])        <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])     <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, sixthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, seventhNext_point]) <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, eigthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, ninthNext_point])    > thresh2:
                    file.values[i, index]             = linearInterpolation(prev_point, index, ninthNext_point)
                    file.values[i, next_point]        = linearInterpolation(prev_point, next_point, ninthNext_point)
                    file.values[i, secNext_point]     = linearInterpolation(prev_point, secNext_point, ninthNext_point)
                    file.values[i, thirdNext_point]   = linearInterpolation(prev_point, thirdNext_point, ninthNext_point)
                    file.values[i, fourthNext_point]  = linearInterpolation(prev_point, fourthNext_point, ninthNext_point)
                    file.values[i, fifthNext_point]   = linearInterpolation(prev_point, fifthNext_point, ninthNext_point)
                    file.values[i, sixthNext_point]   = linearInterpolation(prev_point, sixthNext_point, ninthNext_point)
                    file.values[i, seventhNext_point] = linearInterpolation(prev_point, seventhNext_point, ninthNext_point)
                    file.values[i, eigthNext_point]   = linearInterpolation(prev_point, eigthNext_point, ninthNext_point)
                    #print i, index
                    #print ("ninth 1st derivative condition")
                    index += 9
                    
                elif (index < (num_columns - 10))\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, next_point])        <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, secNext_point])     <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, thirdNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fourthNext_point])  <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, fifthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, sixthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, seventhNext_point]) <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, eigthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, ninthNext_point])   <= thresh2\
                and firstDerivative(file.values[i, prev_point], file.values[i, index], file.values[i, window_bound])       > thresh2:
                    file.values[i, index]             = linearInterpolation(prev_point, index, window_bound)
                    file.values[i, next_point]        = linearInterpolation(prev_point, next_point, window_bound)
                    file.values[i, secNext_point]     = linearInterpolation(prev_point, secNext_point, window_bound)
                    file.values[i, thirdNext_point]   = linearInterpolation(prev_point, thirdNext_point, window_bound)
                    file.values[i, fourthNext_point]  = linearInterpolation(prev_point, fourthNext_point, window_bound)
                    file.values[i, fifthNext_point]   = linearInterpolation(prev_point, fifthNext_point, window_bound)
                    file.values[i, sixthNext_point]   = linearInterpolation(prev_point, sixthNext_point, window_bound)
                    file.values[i, seventhNext_point] = linearInterpolation(prev_point, seventhNext_point, window_bound)
                    file.values[i, eigthNext_point]   = linearInterpolation(prev_point, eigthNext_point, window_bound)
                    file.values[i, ninthNext_point]   = linearInterpolation(prev_point, ninthNext_point, window_bound)
                    #print i, index
                    #print ("tenth 1st derivative condition")
                    index += 10
                    
                 # if there is no noise inside the window, go to next datapoint    
                elif index < num_columns - 1:
                    index += 1
                    
    file = file.drop(range(0,40), axis = 1)                                         # delete 1st 40 points
    file = file.drop(range(num_columns - 5, num_columns), axis = 1)                # delete last 5 points
    # save data to file             
    file.to_csv(destination + str(count) + fileformat, header = False, index = False)
    count += 1
print time.clock() - start, 'seconds taken to execute the program'         