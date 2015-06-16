# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 23:31:44 2015

@author: Shamir
"""
import pandas
#import matplotlib.pyplot as plt
#import numpy as np
from scipy.spatial.distance import euclidean

filepath = 'C:\\Users\\Shamir\\Desktop\\broken down files\\62.csv'

# fileHandler (can become a different class!)
file = pandas.read_csv(filepath, header = None)
file = file.dropna(axis = 1)                                                    # reject every column that contains at least one NaN value (we lose at least one instance of gesture) 
file = file.drop(range(0,40), axis = 1)                                         # delete 1st 40 points          
file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns 

#plt.plot(file.values[32, 0:5])

num_rows = len(file)                                                            # number of rows in the dataset
num_columns = len(file.values[0])                                               # number of columns after preprocessing
column_limit = num_columns - 1                                                  # boundary condition for iterating through columns
thresh = 0.12                                                                   # threshold to find peaks (noisy values based-on euclidean distance)

# function for Linear Interpolation
def linearInterpolation(prev_datapoint, target_datapoint, next_datapoint):
    denominator = next_datapoint - prev_datapoint
    numerator = ((target_datapoint - prev_datapoint) * (file.values[i, next_datapoint] - file.values[i, prev_datapoint]))
    interpolated_value = (numerator/denominator) + file.values[i, prev_datapoint]
    
    return interpolated_value
 
# start denoising every dataset               
for i in range(1, num_rows):
    index = 1                                                                   # index of current datapoint
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
                print ("4th condition")
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
 
# save data to file             
file.to_csv('C:\\Users\\Shamir\\Desktop\\broken down files\\62_denoised.csv', header = False, index = False)
            