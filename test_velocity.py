# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:25:15 2015

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
            #time = number_of_columns / frequency_quat                       # np.shape(readFile.values)[1]
            
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