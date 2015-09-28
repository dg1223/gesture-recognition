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
from itertools import combinations

#source_left = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Left\\'                       # source folder
#source_right = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Right\\'
source_left_sorted = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Left_sorted\\'         # source folder
source_right_sorted = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Right_sorted\\'
filelist_left_sorted = os.listdir(source_left_sorted)
filelist_left_sorted = natsorted(filelist_left_sorted)
filelist_right_sorted = os.listdir(source_right_sorted)
filelist_right_sorted = natsorted(filelist_right_sorted)                                      # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Features\\Left\\'             # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Features\\Right\\'            # gestures performed only with the right hand go here
fileformat = '.csv'
backslash = '\\'
count = 1
frequency_quat = 110                                                            # 110 Hz
frequency_euc  = 82.5                                                           # 82.5 Hz


# function for extracting Variance
def Variance(number_of_rows, sourcePath, Dataset):
    
    for i in range(len(os.listdir(sourcePath))):                                # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                     # Jab, Uppercut, Throw, Jets, Block, Asgard
        dataset = os.listdir(sourcePath + gesture)[Dataset]                     # Dataset: Train = 0, Cross Validation = 1, Test = 2
        copy = False            
        variance_array = []
            
        for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
            sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]                              # Sensor15, Sensor16, Sensor17, Sensor18, Sensor19 
            sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)      # 1.csv ... 4.csv 
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                variance = ['Var_' + sensor[6:] + '_' + readFile.values[0,0]]
                print variance
                variance = np.asarray(variance)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          #  |||len(readFile.values)|||
                    ## need to add code to check if number_of_rows matches                            
                        Var = np.var(readFile.values[m])
                        variance = np.vstack((variance, Var))
                    variance_array = np.hstack((variance_array, variance))                            
                else:
                    for m in range(1, number_of_rows):
                        Var = np.var(readFile.values[m])
                        variance = np.vstack((variance, Var))
                    #covariance_array = np.zeros([len(readFile1.values),1])
                    variance_array = variance.copy()
                    copy = True
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile1 = DataFrame(variance_array)            
        else:
            variance_array = DataFrame(variance_array)
            fullFile1 = pandas.concat([fullFile1, variance_array], join = 'inner')
            
    return fullFile1
        
        
# function for extracting Range       
def Range(number_of_rows, sourcePath, Dataset):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        dataset = os.listdir(sourcePath + gesture)[Dataset]                               # Train, Cross Validation, Test
        copy = False            
        range_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
            sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]
            sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                range_header = ['Range_' + sensor[6:] + '_' + readFile.values[0,0]]
                print range_header
                range_header = np.asarray(range_header)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          # for every two files
                    ## need to add code to check if number_of_rows matches                            
                        Range = np.ptp(readFile.values[m])
                        range_header = np.vstack((range_header, Range))
                    range_array = np.hstack((range_array, range_header))                            
                else:
                    for m in range(1, number_of_rows):
                        Range = np.ptp(readFile.values[m])
                        range_header = np.vstack((range_header, Range))
                    #covariance_array = np.zeros([len(readFile1.values),1])
                    range_array = range_header.copy()
                    copy = True
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile2 = DataFrame(range_array)            
        else:
            range_array = DataFrame(range_array)
            fullFile2 = pandas.concat([fullFile2, range_array], join = 'inner')
            
    return fullFile2
    

# function for extracting Velocity
def Velocity(number_of_rows, number_of_columns, sourcePath, Dataset):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        dataset = os.listdir(sourcePath + gesture)[Dataset]                               # Train, Cross Validation, Test
        copy = False            
        velocity_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
            sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]
            sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                velocity = ['Vel_' + sensor[6:] + '_' + readFile.values[0,0]]
                print velocity
                velocity = np.asarray(velocity)
                distance = 0
                time = number_of_columns / frequency_quat                       # np.shape(readFile.values)[1]
                
                if copy == True:
                    for m in range(1, number_of_rows):                      # for every two files
                        for n in range(number_of_columns - 1):
                    ## need to add code to check if number_of_rows matches 
                            next_index = n + 1
                            distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
                        vel = distance/time
                        velocity = np.vstack((velocity, vel)) 
                    velocity_array = np.hstack((velocity_array, velocity))                                            
                else:
                    for m in range(1, number_of_rows):
                        for n in range(number_of_columns - 1):
                            next_index = n + 1
                            distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
                        vel = distance/time
                        velocity = np.vstack((velocity, vel))
                    velocity_array = velocity.copy()
                    copy = True
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile3 = DataFrame(velocity_array)            
        else:
            velocity_array = DataFrame(velocity_array)
            fullFile3 = pandas.concat([fullFile3, velocity_array], join = 'inner')
            
    return fullFile3


# function for extracting Angular Velocity (uses only one file - combined Euclidean)
def AngularVelocity(number_of_rows, number_of_columns, sourcePath, Dataset):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        dataset = os.listdir(sourcePath + gesture)[Dataset]                                 # Train, Cross Validation, Test
        copy = False            
        AngVel_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
            sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]
            sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                velocityAlpha = ['Alpha_' + sensor[6:] + '_' + readFile.values[0,0]]
                velocityBeta  = ['Beta_'  + sensor[6:] + '_' + readFile.values[0,0]]
                velocityGamma = ['Gamma_' + sensor[6:] + '_' + readFile.values[0,0]]
                print velocityAlpha
                velocityAlpha = np.asarray(velocityAlpha)
                velocityBeta  = np.asarray(velocityBeta)
                velocityGamma = np.asarray(velocityGamma)
                
                time = number_of_columns / frequency_euc                        # np.shape(readFile.values)[1]
                
                if copy == True:                                                # after the 1st iteration, simply start stacking the columns
                    for m in range(1, number_of_rows):                      # len(readFile.values)
                    ## need to add code to check if number_of_rows matches
                        precession, nutation, spin = 0, 0, 0
                        
                        for n in range(0, number_of_columns - 5, 3):
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            alphaNext  = n + 3
                            betaNext   = n + 4          
                            gammaNext  = n + 5
                            precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                            nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                            spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                        precessionVelocity = precession/time
                        nutationVelocity   = nutation/time
                        spinVelocity       = spin/time
                        
                        for n in range(0, number_of_columns - 3, 3):
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            readFile.values[m, alpha] = (precessionVelocity * np.sin(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) + (nutationVelocity * np.cos(readFile.values[m, gamma]))    # alpha component
                            readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) - (nutationVelocity * np.sin(readFile.values[m, gamma]))    # beta component
                            readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, beta])) * spinVelocity                                                                                      # gamma compomemt
                        
                        averageAlpha = np.sum(readFile.values[m, range(0, np.shape(readFile.values)[1], 3)]) / time
                        averageBeta  = np.sum(readFile.values[m, range(1, np.shape(readFile.values)[1], 3)]) / time
                        averageGamma = np.sum(readFile.values[m, range(2, np.shape(readFile.values)[1], 3)]) / time
                        
                        velocityAlpha  = np.vstack((velocityAlpha, averageAlpha))
                        velocityBeta   = np.vstack((velocityBeta,  averageBeta))
                        velocityGamma  = np.vstack((velocityGamma, averageGamma))
                        
                    columnSize = len(velocityAlpha)    
                    angular_velocity = np.zeros((len(velocityAlpha), 3))
                    angular_velocity = angular_velocity.astype(str)             # to avoid string to float conversion error
                    
                    # Return the column vectors in a single 2D array
                    angular_velocity[:,0] = velocityAlpha.reshape(1, columnSize)                          
                    angular_velocity[:,1] = velocityBeta.reshape (1, columnSize)
                    angular_velocity[:,2] = velocityGamma.reshape(1, columnSize)
                    
                    AngVel_array = np.hstack((AngVel_array, angular_velocity))                                                       
                else:
                    for m in range(1, number_of_rows):                      # for every two files
                    ## need to add code to check if number_of_rows matches
                        precession, nutation, spin = 0, 0, 0
                        
                        for n in range(0, number_of_columns - 5, 3):
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            alphaNext  = n + 3
                            betaNext   = n + 4          
                            gammaNext  = n + 5
                            precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                            nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                            spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                        precessionVelocity = precession/time
                        nutationVelocity   = nutation/time
                        spinVelocity       = spin/time
                        
                        for n in range(0, number_of_columns - 3, 3):
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            readFile.values[m, alpha] = (precessionVelocity * np.sin(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) + (nutationVelocity * np.cos(readFile.values[m, gamma]))    # alpha component
                            readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) - (nutationVelocity * np.sin(readFile.values[m, gamma]))    # beta component
                            readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, beta])) * spinVelocity                                                                                      # gamma compomemt
                        
                        averageAlpha = np.sum(readFile.values[m, range(0, np.shape(readFile.values)[1], 3)]) / time
                        averageBeta  = np.sum(readFile.values[m, range(1, np.shape(readFile.values)[1], 3)]) / time
                        averageGamma = np.sum(readFile.values[m, range(2, np.shape(readFile.values)[1], 3)]) / time
                        
                        velocityAlpha  = np.vstack((velocityAlpha, averageAlpha))
                        velocityBeta   = np.vstack((velocityBeta,  averageBeta))
                        velocityGamma  = np.vstack((velocityGamma, averageGamma))
                        
                    columnSize = len(velocityAlpha)    
                    angular_velocity = np.zeros((len(velocityAlpha), 3))
                    angular_velocity = angular_velocity.astype(str)
                    
                    # Return the column vectors in a single 2D array
                    angular_velocity[:,0] = velocityAlpha.reshape(1, columnSize)
                    angular_velocity[:,1] = velocityBeta.reshape (1, columnSize)
                    angular_velocity[:,2] = velocityGamma.reshape(1, columnSize)
                    
                    AngVel_array = angular_velocity.copy()                      # use this array as permanent storage
                    copy = True
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile4 = DataFrame(AngVel_array)            
        else:
            AngVel_array = DataFrame(AngVel_array)
            fullFile4 = pandas.concat([fullFile4, AngVel_array], join = 'inner')
            
    return fullFile4
    
    
def Covariance(number_of_rows, number_of_columns, sourcePath, Dataset):
    
    sensor_combos = np.asarray(list(combinations(range(15,20), 2)))
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        dataset = os.listdir(sourcePath + gesture)[Dataset]                                 # Train, Cross Validation, Test
        copy = False
        covariance_array = []
        
        for k in range(len(sensor_combos)):                                           # we have 10 combinations 
            ## this section can be optimized for greater computational efficiency                
            sensorFolder1 = 'Sensor' + str(sensor_combos[k,0])
            sensorFolder2 = 'Sensor' + str(sensor_combos[k,1])                
            sensor1 = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensorFolder1)        # desired csv files in the folder           
            sensor2 = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensorFolder2)                
            
            for l in range(len(sensor1)):
                csvfile1 = sourcePath + gesture + backslash + dataset + backslash + sensorFolder1 + backslash + sensor1[l]   # full filepath
                csvfile2 = sourcePath + gesture + backslash + dataset + backslash + sensorFolder2 + backslash + sensor2[l]
                readFile1 = pandas.read_csv(csvfile1, header = None)
                readFile2 = pandas.read_csv(csvfile2, header = None)
    
                difference_in_length = np.abs(len(readFile1.values[1]) - len(readFile2.values[1]))
                
                if difference_in_length > 0 and len(readFile1.values[1]) > len(readFile2.values[1]):
                    readFile1 = readFile1.drop(range(0, difference_in_length), axis = 1)
                elif difference_in_length > 0 and len(readFile2.values[1]) > len(readFile1.values[1]):
                    readFile2 = readFile2.drop(range(0, difference_in_length), axis = 1)
                    
                readFile1.values[1:] = readFile1.values[1:].astype(float)
                readFile2.values[1:] = readFile2.values[1:].astype(float)
                
                covariance = ['Cov_' + sensorFolder1[6:] + '_' + sensorFolder2[6:] + '_' + readFile1.values[0,0]]
                print covariance
                covariance = np.asarray(covariance)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          # for every two files; len(readFile1.values)
                    ## need to add code to check if number_of_rows matches                            
                        cov = np.cov(readFile1.values[m], readFile2.values[m], bias = 1)[0,1]
                        covariance = np.vstack((covariance, cov))
                    covariance_array = np.hstack((covariance_array, covariance))                            
                else:
                    for m in range(1, number_of_rows):
                        cov = np.cov(readFile1.values[m], readFile2.values[m], bias = 1)[0,1]
                        covariance = np.vstack((covariance, cov))
                    #covariance_array = np.zeros([len(readFile1.values),1])
                    covariance_array = covariance.copy()
                    copy = True
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile5 = DataFrame(covariance_array)            
        else:
            covariance_array = DataFrame(covariance_array)
            fullFile5 = pandas.concat([fullFile5, covariance_array], join = 'inner')
            
    return fullFile5


def extractFeatures(sourcePath, destinationPath):
    
    # fullFile = pandas.concat([fullFile1, fullFile2, fullFile3, fullFile4, fullFile5], axis = 1)       # comprehensive file structure
    
    for i in range(len(os.listdir(sourcePath))):
        
    
    
    
    