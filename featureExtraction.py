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

source_left         = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P1\\Left\\'                       # source folder
source_right        = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Hands_Sorted\\P1\\Right\\'
source_left_Euclid  = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Left_sorted\\'         # source folder
source_right_Euclid = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Euclidean\\P1\\Right_sorted\\'                                      # naturally sort the file list
destination         = 'C:\\Users\\Shamir\\Desktop\\Grad\\Participant Study\\Feature Extraction\\P1\\'
left                = 'LeftHandFeatures'
right               = 'RightHandFeatures'
fileformat          = '.csv'
backslash           = '\\'
frequency_quat      = 110                                                       # 110 Hz
frequency_euc       = 82.5                                                      # 82.5 Hz



# Calculate the number of missing values in the array 
def CalculateValidData(currentFile, currentRow):                                # currentFile = readFile, currentRow = m          
    number_of_nan = len(currentFile.values[currentRow][pandas.isnull(currentFile.values[currentRow])])           
    length_of_array = len(currentFile.values[currentRow])
    valid_datapoints = length_of_array - number_of_nan    
    return valid_datapoints

# function for extracting Variance
def Variance(sourcePath):
    
    for i in range(len(os.listdir(sourcePath))):                                # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                     # Jab, Uppercut, Throw, Jets, Block, Asgard
        copy = False            
        variance_array = []
            
        for k in range(len(os.listdir(sourcePath + gesture))):
            sensor = os.listdir(sourcePath + gesture)[k]                              # Sensor15, Sensor16, Sensor17, Sensor18, Sensor19 
            sensorFolder = os.listdir(sourcePath + gesture + backslash + sensor)      # 1.csv ... 4.csv 
            sensorFolder = natsorted(sensorFolder)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                number_of_rows = len(readFile.values)
                variance = ['Var_' + sensor[6:] + '_' + readFile.values[0,0]]
                print variance, csvfile[-7:]
                variance = np.asarray(variance)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          #  |||len(readFile.values)|||
                    ## need to add code to check if number_of_rows matches
                        valid_data = CalculateValidData(readFile, m)                # exclude missing values                          
                        Var = np.var(readFile.values[m, 0:valid_data])
                        variance = np.vstack((variance, Var))
                    variance_array = np.hstack((variance_array, variance))                            
                else:
                    for m in range(1, number_of_rows):
                        valid_data = CalculateValidData(readFile, m)
                        Var = np.var(readFile.values[m, 0:valid_data])
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
def Range(sourcePath):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        copy = False            
        range_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture))):
            sensor = os.listdir(sourcePath + gesture)[k]
            sensorFolder = os.listdir(sourcePath + gesture + backslash + sensor)
            sensorFolder = natsorted(sensorFolder)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                number_of_rows    = len(readFile.values)          
                range_header = ['Range_' + sensor[6:] + '_' + readFile.values[0,0]]
                print range_header, csvfile[-7:]
                range_header = np.asarray(range_header)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          # for every two files
                    ## need to add code to check if number_of_rows matches                            
                        valid_data = CalculateValidData(readFile, m)
                        Range = np.ptp(readFile.values[m, 0:valid_data])
                        range_header = np.vstack((range_header, Range))
                    range_array = np.hstack((range_array, range_header))                            
                else:
                    for m in range(1, number_of_rows):
                        valid_data = CalculateValidData(readFile, m)
                        Range = np.ptp(readFile.values[m, 0:valid_data])
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
def Velocity(sourcePath):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        copy = False            
        velocity_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture))):
            sensor = os.listdir(sourcePath + gesture)[k]
            sensorFolder = os.listdir(sourcePath + gesture + backslash + sensor)
            sensorFolder = natsorted(sensorFolder)
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                number_of_rows    = len(readFile.values)
                number_of_columns = np.shape(readFile.values)[1]
                velocity = ['Vel_' + sensor[6:] + '_' + readFile.values[0,0]]
                print velocity, csvfile[-7:]
                velocity = np.asarray(velocity)
                distance = 0
                
                if copy == True:
                    #print 'This is the If phase'
                    for m in range(1, number_of_rows):                      # for every two files
                        for n in range(number_of_columns - 1):
                    ## need to add code to check if number_of_rows matches 
                            next_index = n + 1
                            try:
                                distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
                            except ValueError:
                                #print '(copy = True) at file = ', csvfile[-6:], ', m = ', m, ', n = ', n
                                continue
                            
                        valid_data = CalculateValidData(readFile, m)            # Exclude missing values
                        time = valid_data / frequency_quat
                        
                        vel = distance/time
                        velocity = np.vstack((velocity, vel)) 
                    velocity_array = np.hstack((velocity_array, velocity))
                                             
                else:
                    #print 'This is the Else phase'
                    for m in range(1, number_of_rows):
                        for n in range(number_of_columns - 1):
                            next_index = n + 1
                            try:
                                distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
                            except ValueError:
                                #print '(copy = False) at file = ', csvfile[-6:], ', m = ', m, ', n = ', n
                                continue
                        
                        valid_data = CalculateValidData(readFile, m)            # Exclude missing values
                        time = valid_data / frequency_quat
                        
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
def AngularVelocity(sourcePath):
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        print 'i = ', i    
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        copy = False            
        AngVel_array = []
        
        for k in range(len(os.listdir(sourcePath + gesture))):
            sensor = os.listdir(sourcePath + gesture)[k]            # Sensor15, Sensor16, Sensor17, Sensor18, Sensor19 
            sensorFolder = os.listdir(sourcePath + gesture + backslash + sensor)
            print sensorFolder
            
            for l in range(len(sensorFolder)):
                csvfile = sourcePath + gesture + backslash + sensor + backslash + sensorFolder[l]   # full filepath
                readFile = pandas.read_csv(csvfile, header = None)
                readFile.values[1:] = readFile.values[1:].astype(float)
                
                number_of_rows    = len(readFile.values)
                number_of_columns = np.shape(readFile.values)[1]                
                velocityAlpha = ['Precession_' + sensor[6:]]
                velocityBeta  = ['Nutation_'   + sensor[6:]]
                velocityGamma = ['Spin_'       + sensor[6:]]
                
                velocityAlpha = np.asarray(velocityAlpha)
                velocityBeta  = np.asarray(velocityBeta)
                velocityGamma = np.asarray(velocityGamma)
                
                           
                if copy == True:
                    print 'This is the If phase'
                    for m in range(1, number_of_rows):                      # for every two files ???
                    ## need to add code to check if number_of_rows matches
                        precession, nutation, spin = 0, 0, 0
                                            
                        for n in range(0, number_of_columns - 5, 3):                                                
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            alphaNext  = n + 3
                            betaNext   = n + 4          
                            gammaNext  = n + 5
                            try:    
                                precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                                nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                                spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                            except ValueError:
                            #print '1st catch (copy = True) at file, m, n = ', csvfile[-6:], m, n
                                continue
                        
                        valid_data = CalculateValidData(readFile, m)            # Exclude missing values                 
                        time = valid_data / frequency_euc
                        
                        precessionVelocity = precession/time
                        nutationVelocity   = nutation/time
                        spinVelocity       = spin/time
                                                                
                        for n in range(0, number_of_columns - 3, 3):                                                
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            try:
                                readFile.values[m, alpha] = (precessionVelocity * np.sin(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) + (nutationVelocity * np.cos(readFile.values[m, gamma]))    # alpha component
                                readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) - (nutationVelocity * np.sin(readFile.values[m, gamma]))    # beta component
                                readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, beta])) * spinVelocity                                                                                      # gamma compomemt
                            except ValueError:
                                #print '2nd catch (copy = True) at file, m, n = ', csvfile[-6:], m, n
                                continue
                        
                        averageAlpha = np.sum(readFile.values[m, range(0, valid_data, 3)]) / time
                        averageBeta  = np.sum(readFile.values[m, range(1, valid_data, 3)]) / time
                        averageGamma = np.sum(readFile.values[m, range(2, valid_data, 3)]) / time
                        
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
                    print 'This is the Else phase'
                    for m in range(1, number_of_rows):                      
                    ## need to add code to check if number_of_rows matches
                        precession, nutation, spin = 0, 0, 0
                                                                
                        for n in range(0, number_of_columns - 5, 3):                                                
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            alphaNext  = n + 3
                            betaNext   = n + 4          
                            gammaNext  = n + 5
                            try:                            
                                precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                                nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                                spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                            except ValueError:
                                #print '1st catch (copy = False) at print file, m, n = ', csvfile[-6:], m, n
                                continue
                        
                        valid_data = CalculateValidData(readFile, m)                    
                        time = valid_data / frequency_euc
    
                        precessionVelocity = precession/time                                       
                        nutationVelocity   = nutation/time
                        spinVelocity       = spin/time
                                                                
                        for n in range(0, number_of_columns - 3, 3):                                                
                            alpha      = n
                            beta       = n + 1          
                            gamma      = n + 2
                            try:
                                readFile.values[m, alpha] = (precessionVelocity * np.sin(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) + (nutationVelocity * np.cos(readFile.values[m, gamma]))    # alpha component
                                readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, gamma]) * np.sin(readFile.values[m, beta])) - (nutationVelocity * np.sin(readFile.values[m, gamma]))    # beta component
                                readFile.values[m, beta]  = (precessionVelocity * np.cos(readFile.values[m, beta])) * spinVelocity                                                                                      # gamma compomemt
                            except ValueError:
                                #print '2nd catch (copy = True) at file, m, n = ', csvfile[-6:], m, n
                                continue
                        
                        averageAlpha = np.sum(readFile.values[m, range(0, valid_data, 3)]) / time
                        averageBeta  = np.sum(readFile.values[m, range(1, valid_data, 3)]) / time
                        averageGamma = np.sum(readFile.values[m, range(2, valid_data, 3)]) / time
                        
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
                    
                    AngVel_array = angular_velocity.copy()
                    copy = True
    
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile4 = DataFrame(AngVel_array)            
        else:
            AngVel_array = DataFrame(AngVel_array)
            fullFile4 = pandas.concat([fullFile4, AngVel_array], join = 'inner')
            
    return fullFile4
    
    
def Covariance(sourcePath):
    
    sensor_combos = np.asarray(list(combinations(range(15,20), 2)))
    
    for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
        gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
        copy = False
        covariance_array = []
        
        for k in range(len(sensor_combos)):                                           # we have 10 combinations 
            ## this section can be optimized for greater computational efficiency                
            sensorFolder1 = 'Sensor' + str(sensor_combos[k,0])
            sensorFolder2 = 'Sensor' + str(sensor_combos[k,1])                
            sensor1 = os.listdir(sourcePath + gesture + backslash + sensorFolder1)    # desired csv files in the folder           
            sensor2 = os.listdir(sourcePath + gesture + backslash + sensorFolder2)
            sensor1 = natsorted(sensor1) 
            sensor2 = natsorted(sensor2)               
            
            for l in range(len(sensor1)):
                csvfile1 = sourcePath + gesture + backslash + sensorFolder1 + backslash + sensor1[l]   # full filepath
                csvfile2 = sourcePath + gesture + backslash + sensorFolder2 + backslash + sensor2[l]
                readFile1 = pandas.read_csv(csvfile1, header = None)
                readFile2 = pandas.read_csv(csvfile2, header = None)
                
                readFile1.values[1:] = readFile1.values[1:].astype(float)
                readFile2.values[1:] = readFile2.values[1:].astype(float)
                
                number_of_rows = len(readFile1.values)            
                covariance = ['Cov_' + sensorFolder1[6:] + '_' + sensorFolder2[6:] + '_' + readFile1.values[0,0]]
                print covariance, csvfile1[-7:], csvfile2[-7:]
                covariance = np.asarray(covariance)
                
                if copy == True:
                    for m in range(1, number_of_rows):                          # for every two files; len(readFile1.values)
                    ## need to add code to check if number_of_rows matches
                        valid_data1 = CalculateValidData(readFile1, m)                  # exclude missing values                            
                        valid_data2 = CalculateValidData(readFile2, m)
                        
                        # consider the shorter length for both the arrays to avoid dimension error
                        if valid_data1 > valid_data2:
                            cov = np.cov(readFile1.values[m, 0:valid_data2], readFile2.values[m, 0:valid_data2], bias = 1)[0,1]
                            covariance = np.vstack((covariance, cov))
                        else:
                            cov = np.cov(readFile1.values[m, 0:valid_data1], readFile2.values[m, 0:valid_data1], bias = 1)[0,1]
                            covariance = np.vstack((covariance, cov))
                            
                    covariance_array = np.hstack((covariance_array, covariance))                            
                
                else:
                    for m in range(1, number_of_rows):
                        valid_data1 = CalculateValidData(readFile1, m)
                        valid_data2 = CalculateValidData(readFile2, m)
                        
                        # consider the shorter length for both the arrays to avoid dimension error
                        if valid_data1 > valid_data2:
                            cov = np.cov(readFile1.values[m, 0:valid_data2], readFile2.values[m, 0:valid_data2], bias = 1)[0,1]
                            covariance = np.vstack((covariance, cov))
                        else:
                            cov = np.cov(readFile1.values[m, 0:valid_data1], readFile2.values[m, 0:valid_data1], bias = 1)[0,1]
                            covariance = np.vstack((covariance, cov))
                            
                    covariance_array = covariance.copy()
                    copy = True
                    
        # Create complete file structure/dataframe           
        if i == 0:
            fullFile5 = DataFrame(covariance_array)            
        else:
            covariance_array = DataFrame(covariance_array)
            fullFile5 = pandas.concat([fullFile5, covariance_array], join = 'inner')

    return fullFile5


def extractFeatures():
    
    # Left Hand Gestures
    variance_l = Variance(source_left)
    range_l    = Range(source_left)
    velocity_l = Velocity(source_left)
    AngVel_l   = AngularVelocity(source_left_Euclid)
    covar_l    = Covariance(source_left)
    
    fullFile_l = pandas.concat([variance_l, range_l, velocity_l, AngVel_l, covar_l], axis = 1)
    fullFile_l.to_csv(destination + left + fileformat, header = False, index = False)
    
    # Right Hand Gestures
    variance_r = Variance(source_right)
    range_r    = Range(source_right)
    velocity_r = Velocity(source_right)
    AngVel_r   = AngularVelocity(source_right_Euclid)
    covar_r    = Covariance(source_right)
    
    fullFile_r = pandas.concat([variance_r, range_r, velocity_r, AngVel_r, covar_r], axis = 1)
    fullFile_r.to_csv(destination + right + fileformat, header = False, index = False)
    
extractFeatures()
    
    
    