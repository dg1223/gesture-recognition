# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 21:54:14 2015

@author: Shamir
"""

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