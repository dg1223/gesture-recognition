# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 19:02:15 2015

@author: Shamir
"""
for i in range(1, num_rows):
    euclidean_distance = []
    for j in range(1, num_columns):
        prev_column    = j - 1        
        distance = euclidean(file.values[i, prev_column], file.values[i, j])
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
    corrupted_data = 0
    
    for noise in range(len(noisy_index)):                                 # check for every pair because each pair of euclidean peaks corresponds to one noisy/corrupted datapoint                    
            prev_point    = noisy_index[noise] - 1        
            next_point    = noisy_index[noise] + 1
            secNext_point = noisy_index[noise] + 2
            window_bound  = noisy_index[noise] + 3
            if noise < (len(noisy_index) - 2) and (noisy_index[noise + 1] == noisy_index[noise] + 1):                    # check if it's a pair of adjacent peaks
                if noisy_index[noise + 2] != noisy_index[noise + 1] + 1:
                    file.values[i, noisy_index[noise]] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise], noisy_index[noise] + 1)
                elif noise < (len(noisy_index) - 3) and (noisy_index[noise + 3] != noisy_index[noise + 2] + 1):
                    file.values[i, noisy_index[noise]] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise], noisy_index[noise] + 2)
                    file.values[i, noisy_index[noise] + 1] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise] + 1, noisy_index[noise] + 2)
                else:
                    file.values[i, noisy_index[noise]] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise], noisy_index[noise] + 3)
                    file.values[i, noisy_index[noise] + 1] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise] + 1, noisy_index[noise] + 3)
                    file.values[i, noisy_index[noise] + 2] = linearInterpolation(noisy_index[noise] - 1, noisy_index[noise] + 2, noisy_index[noise] + 3)
