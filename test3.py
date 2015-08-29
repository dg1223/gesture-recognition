# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:07:11 2015

@author: Shamir
"""

for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
    
    for j in range(len(os.listdir(sourcePath + gesture))):                            # we have 3 files corresponding to 3 datasets (train, cross-validation, test)
        dataset = os.listdir(sourcePath + gesture)[j]                                 # Train, Cross Validation, Test
        copy = False
        
        #a_sensor_folder = os.listdir(sourcePath + gesture + backslash + dataset + backslash)[0]
        #a_file_in_dataset = os.listdir(sourcePath + gesture + backslash + dataset + backslash + a_sensor_folder)[0]
        #read_the_file = pandas.read_csv(sourcePath + gesture + backslash + dataset + backslash + a_sensor_folder + backslash + a_file_in_dataset)
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
                    for m in range(1, len(readFile1.values)):                      # for every two files
                    ## need to add code to check if number_of_rows matches                            
                        cov = np.cov(readFile1.values[m], readFile2.values[m], bias = 1)[0,1]
                        covariance = np.vstack((covariance, cov))
                    covariance_array = np.hstack((covariance_array, covariance))                            
                else:
                    for m in range(1, len(readFile1.values)):
                        cov = np.cov(readFile1.values[m], readFile2.values[m], bias = 1)[0,1]
                        covariance = np.vstack((covariance, cov))
                    #covariance_array = np.zeros([len(readFile1.values),1])
                    covariance_array = covariance.copy()
                    copy = True