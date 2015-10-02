# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 21:08:13 2015

@author: Shamir
"""

# Calculate the number of missing values in the array 
def CalculateValidData(currentFile, currentRow):                                # currentFile = readFile, currentRow = m          
    number_of_nan = len(currentFile.values[currentRow][pandas.isnull(currentFile.values[currentRow])])           
    length_of_array = len(currentFile.values[currentRow])
    valid_datapoints = length_of_array - number_of_nan    
    return valid_datapoints
        
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