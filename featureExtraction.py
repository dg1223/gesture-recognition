# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 21:18:52 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
from natsort import natsorted
from pandas import DataFrame
from scipy.spatial.distance import euclidean

source_left = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Left\\'                       # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Right\\'
filelist_left = os.listdir(source_left)
filelist_left = natsorted(filelist_left)
filelist_right = os.listdir(source_right)
filelist_right = natsorted(filelist_right)                                      # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Features\\Left\\'             # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Features\\Right\\'            # gestures performed only with the right hand go here
fileformat = '.csv'
count = 1
frequency_quat = 110                                                            # 110 Hz
frequency_euc  = 82.5                                                           # 82.5 Hz


# function for extracting Variance
def Variance(number_of_rows, sourceFile):
    
    variance = ['variance']
    variance = np.asarray(variance)
    for i in range(1, number_of_rows):
        Var = np.var(sourceFile.values[i])
        variance = np.vstack((variance, Var))
    return variance
        
        
# function for extracting Range       
def Range(number_of_rows, sourceFile):
    
    range_of_row = ['range']
    range_of_row = np.asarray(range_of_row)
    for i in range(1, number_of_rows):
        ran = np.ptp(sourceFile.values[i])
        range_of_row = np.vstack((range_of_row, ran))
    return range_of_row


# function for extracting Velocity
def Velocity(number_of_rows, number_of_columns, sourceFile):
    
    velocity = ['velocity']
    velocity = np.asarray(velocity)
    distance = 0
    time = number_of_columns / frequency_quat                                              
    for i in range(1, number_of_rows):         
        for j in range(number_of_columns - 1):
            next = j + 1
            distance += euclidean(sourceFile.values[i, j], sourceFile.values[i, next])
        vel = distance/time
        velocity = np.vstack((velocity, vel))
    return velocity


# function for extracting Angular Velocity
def AngularVelocity(number_of_rows, number_of_columns, sourceFile):
    
    velocityAlpha  = ['velocityAlpha']
    velocityBeta   = ['velocityBeta']
    velocityGamma  = ['velocityGamma']
    velocityAlpha  = np.asarray(velocityAlpha)
    velocityBeta   = np.asarray(velocityBeta)
    velocityGamma  = np.asarray(velocityGamma)
    time = number_of_columns / frequency_euc
    for i in range(1, number_of_rows):
        precession, nutation, spin = 0, 0, 0
                         
        for j in range(0, number_of_columns - 5, 3):            
            alpha      = j
            beta       = j + 1          
            gamma      = j + 2
            alphaNext  = j + 3
            betaNext   = j + 4          
            gammaNext  = j + 5
            precession += euclidean(sourceFile.values[i, alpha], sourceFile.values[i, alphaNext])
            nutation   += euclidean(sourceFile.values[i, beta],  sourceFile.values[i, betaNext])
            spin       += euclidean(sourceFile.values[i, gamma], sourceFile.values[i, gammaNext])
        precessionVelocity = precession/time
        nutationVelocity   = nutation/time
        spinVelocity       = spin/time
        
        for j in range(0, number_of_columns - 3, 3):
            alpha      = j
            beta       = j + 1          
            gamma      = j + 2
            sourceFile.values[i, alpha] = (precessionVelocity * np.sin(sourceFile.values[i, gamma]) * np.sin(sourceFile.values[i, beta])) + (nutationVelocity * np.cos(sourceFile.values[i, gamma]))    # alpha component
            sourceFile.values[i, beta]  = (precessionVelocity * np.cos(sourceFile.values[i, gamma]) * np.sin(sourceFile.values[i, beta])) - (nutationVelocity * np.sin(sourceFile.values[i, gamma]))    # beta component
            sourceFile.values[i, beta]  = (precessionVelocity * np.cos(sourceFile.values[i, beta])  * spinVelocity                                                                                      # gamma compomemt
        
        averageAlpha = np.sum(sourceFile.values[i, range(0, number_of_columns, 3)]) / time
        averageBeta  = np.sum(sourceFile.values[i, range(1, number_of_columns, 3)]) / time
        averageGamma = np.sum(sourceFile.values[i, range(2, number_of_columns, 3)]) / time
        
        velocityAlpha  = np.vstack((velocityAlpha, averageAlpha))
        velocityBeta   = np.vstack((velocityBeta,  averageBeta))
        velocityGamma  = np.vstack((velocityGamma, averageGamma))
        
    
    return

def extractFeatures(filelist, sourcePath, destinationPath):
    
    for eachfile in range(len(filelist)):               # len(filelist)

        csvfile = source + filelist[eachfile]                                       # full filepath
        file = pandas.read_csv(csvfile, header = None)
        file.values[1:] = file.values[1:].astype(float)                             # convert all strings to floats; ignore header columns
        num_rows = len(file)                                                        # number of rows in the dataset
        num_columns = len(file.values[0])
        # calculate variance
        
        