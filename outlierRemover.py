# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 23:31:44 2015

@author: Shamir
"""
import pandas
#import matplotlib.pyplot as plt
#import numpy as np
from scipy.spatial.distance import euclidean

filepath = 'C:\\Users\\Shamir\\Desktop\\broken down files\\1_test.csv'

# fileHandler (can become a different class!)
file = pandas.read_csv(filepath, header = None)
file = file.dropna(axis = 1)                                                    # reject every column that contains at least one NaN value (we lose at least one instance of gesture) 
file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns 

#plt.plot(file.values[32, 0:5])

num_rows = len(file)
num_columns = len(file.values[0])
column_limit = num_columns - 1
thresh = 0.15

def linearInterpolation(prev_datapoint, target_datapoint, next_datapoint):
    denominator = next_datapoint - prev_datapoint
    numerator = ((target_datapoint - prev_datapoint) * (file.values[i, next_datapoint] - file.values[i, prev_datapoint]))
    interpolated_value = (numerator/denominator) + file.values[i, prev_datapoint]
    
    return interpolated_value
                   
for i in range(1, num_rows):
    index = 1
    for j in range(num_columns):
        if index == num_columns - 1:
            #print ("error: index == num_columns - 1")
            break        
        else:     
            prev_point      = index - 1                                         # prev_point (1), index (2), next_point (3), secNext_point (4), thirdNext_point (5), window_bound (6)
            next_point      = index + 1
            secNext_point   = index + 2
            thirdNext_point = index + 3
            window_bound    = index + 4
            if (index < (num_columns - 1)) and (euclidean(file.values[i, index], file.values[i, prev_point]) <= thresh):
                #print ("0th condition")
                index += 1
                
            elif (index < (num_columns - 1)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
            and euclidean(file.values[i, next_point], file.values[i, prev_point]) <= thresh:
                print ("1st condition")
                file.values[i, index] = linearInterpolation(prev_point, index, next_point)
                index += 2
        
            elif (index < (num_columns - 2)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
            and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) <= thresh):
                file.values[i, index] = linearInterpolation(prev_point, index, secNext_point)
                file.values[i, next_point] = linearInterpolation(prev_point, next_point, secNext_point)
                print ("2nd condition")
                index += 3
                
            elif (index < (num_columns - 3)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
            and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) > thresh)\
            and (euclidean(file.values[i, thirdNext_point], file.values[i, prev_point]) <= thresh):
                file.values[i, index] = linearInterpolation(prev_point, index, thirdNext_point)
                #print file.values[i, index]
                file.values[i, next_point] = linearInterpolation(prev_point, next_point, thirdNext_point)
                #print file.values[i, next_point]
                file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, thirdNext_point)
                #print file.values[i, secNext_point]
                print ("3rd condition")
                index += 4
                
            elif (index < (num_columns - 4)) and (euclidean(file.values[i, index], file.values[i, prev_point]) > thresh)\
            and (euclidean(file.values[i, next_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, secNext_point], file.values[i, prev_point]) > thresh)\
            and (euclidean(file.values[i, thirdNext_point], file.values[i, prev_point]) > thresh) and (euclidean(file.values[i, window_bound], file.values[i, prev_point]) <= thresh):
                file.values[i, index] = linearInterpolation(prev_point, index, window_bound)
                file.values[i, next_point] = linearInterpolation(prev_point, next_point, window_bound)
                file.values[i, secNext_point] = linearInterpolation(prev_point, secNext_point, window_bound)
                file.values[i, thirdNext_point] = linearInterpolation(prev_point, thirdNext_point, window_bound)
                print ("4th condition")
                index += 5
            #else:
                #continue
    #print ("prev_point = "), prev_point    
    #print ("index = "), index    
    #print ("next_point = "), next_point
    
#plt.plot(file.values[32, 0:5])               
#==============================================================================
#         if (index < (num_columns - 3)) and file.values[i, secNext_point] != file.values[i, next_point]:
#             distance = euclidean(file.values[i, prev_point], file.values[i, index])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, next_point])
#             euclidean_distance.append(distance)
#             index += 2
#         elif (index < (num_columns - 4)) and file.values[i, thirdNext_point] != file.values[i, secNext_point]:
#             distance = euclidean(file.values[i, prev_point], file.values[i, index])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, next_point])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, secNext_point])
#             euclidean_distance.append(distance)
#             index += 3
#         elif (index < (num_columns - 5)) and file.values[i, window_bound] != file.values[i, thirdNext_point]:
#             distance = euclidean(file.values[i, prev_point], file.values[i, index])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, next_point])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, secNext_point])
#             euclidean_distance.append(distance)
#             distance = euclidean(file.values[i, prev_point], file.values[i, thirdNext_point])
#             euclidean_distance.append(distance)
#             index += 4
#         elif index < (num_columns - 1):
#             distance = euclidean(file.values[i, prev_point], file.values[i, index])
#             euclidean_distance.append(distance)
#             index += 1
#     #print index
#     euclidean_distance = np.asarray(euclidean_distance)
#     #print euclidean_distance.max()
# 
#       if euclidean_distance.max() < 0.15:
#           continue
#       else:
#           threshold = euclidean_distance.max() * 0.2
#           noisy_data = euclidean_distance[euclidean_distance > threshold]
#           noisy_index = []
#           
#           for k in range(len(noisy_data)):
#               noisy_index.append(np.where(euclidean_distance == noisy_data[k])[0][0] + 1)
#               if k > 0:                                                           # compare with previous index value to...
#                   if noisy_index[k] == noisy_index[k-1]:                          # check if index values are same because of identical values of adjacent datapoints in the actual dataset
#                       noisy_index[k] = noisy_index[k] + 1                         # increment index value by 1 to capture the accurate index
#           noisy_index = np.asarray(noisy_index)
#           print i
#           print noisy_index
#           peak_width = []
#           width_counter, index = 0, 0
#           for noise in range(len(noisy_index)):                                   # check for every pair because each pair of euclidean peaks corresponds to one noisy/corrupted datapoint
#               next_point    = index + 1
#               secNext_point = index + 2
#               window_bound  = index + 3
#               if index == len(noisy_index) - 1:                                   # break loop if it's the end of row
#                   break
#               elif index > 0:
#                   if width_counter <= len(peak_width):
#                       index += peak_width[width_counter - 1]
#                       if index < len(noisy_index) - 1 and noisy_index[index+1] == noisy_index[index] + 1:
#                           peak_width.append(1)
#                           if index < len(noisy_index) - 2 and noisy_index[index+2] == noisy_index[index+1] + 1:
#                               peak_width[width_counter] = 2
#                               if index < len(noisy_index) - 3 and noisy_index[index+3] == noisy_index[index+2] + 1:
#                                   peak_width[width_counter] = 3
#                       width_counter += 1
#                       index += 1
#                       if index > len(noisy_index):
#                           break
#               else:                                                               # noise = 0                
#                   peak_width.append(1)                                            # minimum peak width = 1
#                   if index < len(noisy_index) - 2 and noisy_index[index+2] == noisy_index[index+1] + 1:
#                       peak_width[width_counter] = 2
#                       if index < len(noisy_index) - 3 and noisy_index[index+3] == noisy_index[index+2] + 1:
#                           peak_width[width_counter] = 3
#                   width_counter += 1
#                   index += 1
#       
#           index = 0
#           for peak in range(len(peak_width)):                                     # check for every pair because each pair of euclidean peaks corresponds to one noisy/corrupted datapoint                       
#               prev_point    = noisy_index[noise] - 1        
#               next_point    = noisy_index[noise] + 1
#               secNext_point = noisy_index[noise] + 2
#               window_bound  = noisy_index[noise] + 3
#               if peak_width[peak] == 1:
#                       file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 1)
#                       index += 2
#               if peak_width[peak] == 2:
#                       file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 2)
#                       file.values[i, noisy_index[index] + 1] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 1, noisy_index[index] + 2)
#                       index += 3
#               if peak_width[peak] == 3:
#                       file.values[i, noisy_index[index]] = linearInterpolation(noisy_index[index] - 1, noisy_index[index], noisy_index[index] + 3)
#                       file.values[i, noisy_index[index] + 1] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 1, noisy_index[index] + 3)
#                       file.values[i, noisy_index[index] + 2] = linearInterpolation(noisy_index[index] - 1, noisy_index[index] + 2, noisy_index[index] + 3)
#==============================================================================
                      #index += 4
              
file.to_csv('C:\\Users\\Shamir\\Desktop\\broken down files\\1_test1.csv', header = False, index = False)
            