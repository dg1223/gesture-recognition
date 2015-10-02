# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 20:54:02 2015

@author: Shamir
"""

# Calculate the number of missing values in the array 
def CalculateValidData(currentFile, currentRow):                                # currentFile = readFile, currentRow = m          
    number_of_nan = len(currentFile.values[currentRow][pandas.isnull(currentFile.values[currentRow])])           
    length_of_array = len(currentFile.values[currentRow])
    valid_datapoints = length_of_array - number_of_nan    
    return valid_datapoints

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