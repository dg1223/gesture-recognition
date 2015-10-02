# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 19:43:07 2015

@author: Shamir
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 01 19:26:11 2015

@author: Shamir
"""

# Calculate the number of missing values in the array 
def CalculateValidData(currentFile, currentRow):                                # currentFile = readFile, currentRow = m          
    number_of_nan = len(currentFile.values[currentRow][pandas.isnull(currentFile.values[currentRow])])           
    length_of_array = len(currentFile.values[currentRow])
    valid_datapoints = length_of_array - number_of_nan    
    return valid_datapoints
    
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