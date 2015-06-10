# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 15:43:13 2015

@author: Shamir
"""

import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import pandas

def butter_lowpass(cutoff, fs, order=1):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=1):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Filter requirements.
order = 1
fs = 60.0       # sample rate, Hz
cutoff = 1  # desired cutoff frequency of the filter, Hz

#==============================================================================
# # Get the filter coefficients so we can check its frequency response.
# b, a = butter_lowpass(cutoff, fs, order)
# 
# # Plot the frequency response.
# w, h = freqz(b, a, worN=8000)
# plt.subplot(2, 1, 1)
# plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
# plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
# plt.axvline(cutoff, color='k')
# plt.xlim(0, 0.5*fs)
# plt.title("Lowpass Filter Frequency Response")
# plt.xlabel('Frequency [Hz]')
#==============================================================================
#plt.grid()

    

filepath = 'C:\\Users\\Shamir\\Desktop\\broken down files\\1.csv'
# 
# fileHandler (can become a different class!)
file = pandas.read_csv(filepath, header = None)
file = file.dropna(axis = 1)                                                    # reject every column that contains at least one NaN value (we lose at least one instance of gesture) 
file.values[1:] = file.values[1:].astype(float)                                 # convert all strings to floats; ignore header columns 

filtered_array = butter_lowpass_filter(file.values[1:], cutoff, fs, order)
final_data = pandas.DataFrame(data = filtered_array)
#    
#plt.plot(file.values[1])
final_data.to_csv('C:\\Users\\Shamir\\Desktop\\broken down files\\1_butter2.csv', header = False, index = False)

