# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:07:11 2015

@author: Shamir
"""
         
def CalculateValidData():
    # Calculate the number of missing values in the array                    
    number_of_nan = len(readFile.values[m][pandas.isnull(readFile.values[m])])           
    length_of_array = len(readFile.values[m])
    valid_datapoints = length_of_array - number_of_nan    
    return valid_datapoints
    
    
for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
    print 'i = ', i    
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
    #dataset = os.listdir(sourcePath + gesture)[0]                                     # Train, Cross Validation, Test
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
            
            velocityAlpha = ['Precession_' + sensor[6:]]
            velocityBeta  = ['Nutation_'   + sensor[6:]]
            velocityGamma = ['Spin_'       + sensor[6:]]
            #print velocityAlpha
            velocityAlpha = np.asarray(velocityAlpha)
            velocityBeta  = np.asarray(velocityBeta)
            velocityGamma = np.asarray(velocityGamma)
            
            #time = np.shape(readFile.values)[1] / frequency_euc
            
                       
            if copy == True:
                print 'This is the If phase'
                for m in range(1, len(readFile.values)):                      # for every two files ???
                ## need to add code to check if number_of_rows matches
                    precession, nutation, spin = 0, 0, 0
                                        
                    for n in range(0, np.shape(readFile.values)[1] - 5, 3):                                                
                        alpha      = n
                        beta       = n + 1          
                        gamma      = n + 2
                        alphaNext  = n + 3
                        betaNext   = n + 4          
                        gammaNext  = n + 5
                        try:    
                            precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                            #print 'precession = ', precession
                            nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                            spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                        except ValueError:
                        #print '1st catch (copy = True) at file, m, n = ', csvfile[-6:], m, n
                            break
                    
                    valid_data = CalculateValidData()                           # Exclude missing values (we exclude 6 more values to remain within a safer margin)                    
                    time = valid_data / frequency_euc
                    
                    precessionVelocity = precession/time
                    #print 'precessionVelocity = ', precessionVelocity
                    nutationVelocity   = nutation/time
                    spinVelocity       = spin/time
                                                            
                    for n in range(0, np.shape(readFile.values)[1] - 3, 3):                                                
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
                    #print 'filename, m, velocityAlpha = ', csvfile[-6:], m, velocityAlpha
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
                #print 'AngVel_array = ', AngVel_array                                                       
            else:
                print 'This is the Else phase'
                for m in range(1, len(readFile.values)):                      # for every two files
                ## need to add code to check if number_of_rows matches
                    precession, nutation, spin = 0, 0, 0
                                                            
                    for n in range(0, np.shape(readFile.values)[1] - 5, 3):                                                
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
                    
                    valid_data = CalculateValidData()                    
                    time = valid_data / frequency_euc

                    precessionVelocity = precession/time                                       
                    nutationVelocity   = nutation/time
                    spinVelocity       = spin/time
                    #print 'precession,nutation,spinVelocity = ', precessionVelocity, nutationVelocity, spinVelocity
                                                            
                    for n in range(0, np.shape(readFile.values)[1] - 3, 3):                                                
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
                    #print 'averageAlpha = ', averageAlpha
                    averageBeta  = np.sum(readFile.values[m, range(1, valid_data, 3)]) / time
                    averageGamma = np.sum(readFile.values[m, range(2, valid_data, 3)]) / time
                    
                    velocityAlpha  = np.vstack((velocityAlpha, averageAlpha))
                    #print 'filename, m, velocityAlpha = ', csvfile[-6:], m, velocityAlpha
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
                #print 'AngVel_array = ', AngVel_array
                copy = True

    # Create complete file structure/dataframe           
    if i == 0:
        fullFile4 = DataFrame(AngVel_array)            
    else:
        AngVel_array = DataFrame(AngVel_array)
        fullFile4 = pandas.concat([fullFile4, AngVel_array], join = 'inner')
