# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 23:31:44 2015

@author: Shamir
"""
import pandas
import numpy as np
from scipy.spatial.distance import euclidean

filepath = 'C:\\Users\\Shamir\\Desktop\\broken down files\\1.csv'

# fileHandler (can become a different class!)
file = pandas.read_csv(filepath, header = None)
file = file.dropna(axis = 1)                                                    # reject every column that contains at least one NaN value (we lose at least one instance of gesture) 
file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns 

num_rows = len(file)
num_columns = len(file.values[0])
column_limit = num_columns - 1                                                  # end of row

def linearInterpolation(prev_datapoint, target_datapoint, next_datapoint):
    denominator = next_datapoint - prev_datapoint
    numerator = ((target_datapoint - prev_datapoint) * (file.values[i, next_datapoint] - file.values[i, prev_datapoint]))
    interpolated_value = (numerator/denominator) + file.values[i, prev_datapoint]
    
    return interpolated_value

# run Linear Interpolation 4 times
#for a in range(1):
#for i in range(1, num_rows):                                                # ignore headers by starting from 0
        # convert max and min values of this row to their absolutes
#==============================================================================
#         row_max_absolute = abs(file.values[i].max())
#         print "max = ", row_max_absolute
#         row_min_absolute = abs(file.values[i].min())
#         print "min= ", row_min_absolute
#==============================================================================
                
#==============================================================================
#         # calculate threshold value for interpolation's condition
#         if row_min_absolute > row_max_absolute:
#             threshold = row_min_absolute * 0.2                                  # threshold to perform linear interpolation
#             print "threshold = ", threshold
#         else:
#             threshold = row_max_absolute * 0.2
#             print "threshold = ", threshold
#==============================================================================

#==============================================================================
# for i in range(1, num_rows):      
#     for j in range(1, num_columns):                                         # number of columns is the same for every row
#         if j == column_limit - 2:                                           # target datapoint reaches end of row  
#             break
#         else:
#             prev_point    = j - 1                                           # To speed up calculations inside for loop by preventing any calculation on the left hand side (memory access)
#             next_point    = j + 1                                           # j - 1, j,  j + 1
#             secNext_point = j + 2
#             window_bound  = j + 3
#                                                                                 # prev_datapoint, j and next_datapoint indicate their corresponding column numbers        
#             # modified linear interpolation (sliding window method) if target is greater than threshold        
#             if np.abs(file.values[i,j]) > threshold :                       # if n + 1 > 0.2 * max(corresponding row), i.e. 20% of the maximum value of the datapoints in that row [not the most robust formula] 
#                 if np.abs(file.values[i,next_point]) <= threshold:
#                     #file.values[i,j] = next_point
#                     file.values[i,j] = linearInterpolation(prev_point, j, next_point)
#                 elif np.abs(file.values[i,secNext_point]) <= threshold:
#                     #file.values[i,j] = secNext_point
#                     #file.values[i,j] = 
#                     file.values[i,j] = linearInterpolation(prev_point, j, secNext_point)
#                     file.values[i, next_point] = linearInterpolation(j, next_point, secNext_point)
#                 else:                    
#                     file.values[i,j] = linearInterpolation(prev_point, j, window_bound)
#                     file.values[i, next_point] = linearInterpolation(j, next_point, window_bound)
#                     file.values[i, secNext_point] = linearInterpolation(next_point, secNext_point, window_bound)   
#==============================================================================
                    
euclidean_distance = []
for i in range(1, num_rows):
    for j in range(1, num_columns):
        prev_point    = j - 1        
        distance = euclidean(file.values[i, prev_point], file.values[i, j])
        euclidean_distance.append(distance)
        
    euclidean_distance = np.asarray(euclidean_distance)   
    threshold = euclidean_distance.max() * 0.2
    noisy_data = euclidean_distance[euclidean_distance > threshold]
    noisy_index = []
    
    for k in range(len(noisy_data)):
        noisy_index.append(np.where(euclidean_distance == noisy_data[k])[0][0] + 1)
        if k > 0:                                                               # compare with previous index value to...
            if noisy_index[k] == noisy_index[k-1]:                              # check if index values are same because of identical values of adjacent datapoints in the actual dataset
                noisy_index[k] = noisy_index[k] + 1                             # increment index value by 1 to capture the accurate index
    noisy_index = np.asarray(noisy_index)
    
    peak_width = []
    width_counter, index = 0, 0
    for noise in range(len(noisy_index)):                                 # check for every pair because each pair of euclidean peaks corresponds to one noisy/corrupted datapoint
        if index == len(noisy_index) - 1:                                       # break loop if it's the end of row
            break
        elif index > 0:
            index += peak_width[width_counter - 1]
            if index < len(noisy_index) - 1 and noisy_index[index+1] == noisy_index[index] + 1:
                peak_width.append(1)
                if index < len(noisy_index) - 2 and noisy_index[index+2] == noisy_index[index+1] + 1:
                    peak_width[width_counter] = 2
                    if index < len(noisy_index) - 3 and noisy_index[index+3] == noisy_index[index+2] + 1:
                        peak_width[width_counter] = 3
            width_counter += 1
            index += 1
            if index > len(noisy_index):
                break
        else:                                                                   # noise = 0                
            peak_width.append(1)                                                # minimum peak width = 1
            if index < len(noisy_index) - 2 and noisy_index[index+2] == noisy_index[index+1] + 1:
                peak_width[width_counter] = 2
                if index < len(noisy_index) - 3 and noisy_index[index+3] == noisy_index[index+2] + 1:
                    peak_width[width_counter] = 3
            width_counter += 1
            index += 1

index = 0
for peak in range(len(peak_width)):                                 # check for every pair because each pair of euclidean peaks corresponds to one noisy/corrupted datapoint                       
    prev_point    = noisy_index[noise] - 1        
    next_point    = noisy_index[noise] + 1
    secNext_point = noisy_index[noise] + 2
    window_bound  = noisy_index[noise] + 3
    if peak_width[peak] == 1:
            file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 1)
            index += 2
    if peak_width[peak] == 2:
            file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 2)
            file.values[i, noisy_index[index] + 1] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 1, noisy_index[index] + 2)
            index += 3
    if peak_width[peak] == 3:
            file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 3)
            file.values[i, noisy_index[index] + 1] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 1, noisy_index[index] + 3)
            file.values[i, noisy_index[index] + 2] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 2, noisy_index[index] + 3)
            index += 4
            
file.to_csv('C:\\Users\\Shamir\\Desktop\\broken down files\\1_test.csv', header = False, index = False)
            
            