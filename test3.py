# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 00:07:11 2015

@author: Shamir
"""
#==============================================================================
# 
# for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
#     gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
#     dataset = os.listdir(sourcePath + gesture)[0]                               # Dataset: Train = 0, Cross Validation = 1, Test = 2
#     copy = False            
#     variance_array = []
#         
#     for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
#         sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]                              # Sensor15, Sensor16, Sensor17, Sensor18, Sensor19 
#         sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)      # 1.csv ... 4.csv 
#         
#         for l in range(len(sensorFolder)):
#             csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
#             readFile = pandas.read_csv(csvfile, header = None)
#             readFile.values[1:] = readFile.values[1:].astype(float)
#             
#             variance = ['Var_' + sensor[6:] + '_' + readFile.values[0,0]]
#             print variance
#             variance = np.asarray(variance)
#             
#             if copy == True:
#                 for m in range(1, len(readFile.values)):                          #  |||len(readFile.values)|||
#                 ## need to add code to check if number_of_rows matches                            
#                     Var = np.var(readFile.values[m])
#                     variance = np.vstack((variance, Var))
#                 variance_array = np.hstack((variance_array, variance))                            
#             else:
#                 for m in range(1, len(readFile.values)):
#                     Var = np.var(readFile.values[m])
#                     variance = np.vstack((variance, Var))
#                 #covariance_array = np.zeros([len(readFile1.values),1])
#                 variance_array = variance.copy()
#                 copy = True
#     if i == 0:
#         fullFile = DataFrame(variance_array)            
#     else:
#         variance_array = DataFrame(variance_array)
#         fullFile = pandas.concat([fullFile, variance_array], join = 'inner')
#==============================================================================
#==============================================================================
#         
#         
# for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
#     gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
#     dataset = os.listdir(sourcePath + gesture)[0]                               # Train, Cross Validation, Test
#     copy = False            
#     velocity_array = []
#     
#     for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
#         sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]
#         sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)
#         
#         for l in range(len(sensorFolder)):
#             csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
#             readFile = pandas.read_csv(csvfile, header = None)
#             readFile.values[1:] = readFile.values[1:].astype(float)
#             
#             velocity = ['Vel_' + sensor[6:] + '_' + readFile.values[0,0]]
#             print velocity
#             velocity = np.asarray(velocity)
#             distance = 0
#             time = np.shape(readFile.values)[1] / frequency_quat
#             
#             if copy == True:
#                 for m in range(1, len(readFile.values)):                      # for every two files
#                     for n in range(np.shape(readFile.values)[1] - 1):
#                 ## need to add code to check if number_of_rows matches 
#                         next_index = n + 1
#                         distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
#                     vel = distance/time
#                     velocity = np.vstack((velocity, vel)) 
#                 velocity_array = np.hstack((velocity_array, velocity))                                            
#             else:
#                 for m in range(1, len(readFile.values)):                        # len(readFile.values)
#                     for n in range(np.shape(readFile.values)[1] - 1):
#                         next_index = n + 1
#                         distance += euclidean(readFile.values[m, n], readFile.values[m, next_index])
#                     vel = distance/time
#                     velocity = np.vstack((velocity, vel))
#                 velocity_array = velocity.copy()
#                 copy = True
#     # Create complete file structure/dataframe           
#     if i == 0:
#         fullFile3 = DataFrame(velocity_array)            
#     else:
#         velocity_array = DataFrame(velocity_array)
#==============================================================================
#==============================================================================
#         fullFile3 = pandas.concat([fullFile3, velocity_array], join = 'inner')
#         
#         
#==============================================================================
#==============================================================================
         
for i in range(len(os.listdir(sourcePath))):                                          # we have 6 files corresponding to 6 gestures
    gesture = os.listdir(sourcePath)[i]                                               # Jab, Uppercut, Throw, Jets, Block, Asgard
    dataset = os.listdir(sourcePath + gesture)[0]                                     # Train, Cross Validation, Test
    copy = False            
    AngVel_array = []
    
    for k in range(len(os.listdir(sourcePath + gesture + backslash + dataset))):
        sensor = os.listdir(sourcePath + gesture + backslash + dataset)[k]            # Sensor15, Sensor16, Sensor17, Sensor18, Sensor19 
        sensorFolder = os.listdir(sourcePath + gesture + backslash + dataset + backslash + sensor)
        
        for l in range(len(sensorFolder)):
            csvfile = sourcePath + gesture + backslash + dataset + backslash + sensor + backslash + sensorFolder[l]   # full filepath
            readFile = pandas.read_csv(csvfile, header = None)
            readFile.values[1:] = readFile.values[1:].astype(float)
            
            velocityAlpha = ['Precession_' + sensor[6:]]
            velocityBeta  = ['Nutation_'   + sensor[6:]]
            velocityGamma = ['Spin_'       + sensor[6:]]
            print velocityAlpha
            velocityAlpha = np.asarray(velocityAlpha)
            velocityBeta  = np.asarray(velocityBeta)
            velocityGamma = np.asarray(velocityGamma)
            
            time = np.shape(readFile.values)[1] / frequency_euc
            
            if copy == True:
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
                        precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                        nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                        spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                    precessionVelocity = precession/time
                    nutationVelocity   = nutation/time
                    spinVelocity       = spin/time
                    
                    for n in range(0, np.shape(readFile.values)[1] - 3, 3):
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
                        precession += euclidean(readFile.values[m, alpha], readFile.values[m, alphaNext])
                        nutation   += euclidean(readFile.values[m, beta],  readFile.values[m, betaNext])
                        spin       += euclidean(readFile.values[m, gamma], readFile.values[m, gammaNext])
                    precessionVelocity = precession/time
                    nutationVelocity   = nutation/time
                    spinVelocity       = spin/time
                    
                    for n in range(0, np.shape(readFile.values)[1] - 3, 3):
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
                
                AngVel_array = angular_velocity.copy()
                copy = True
    # Create complete file structure/dataframe           
    if i == 0:
        fullFile4 = DataFrame(AngVel_array)            
    else:
        AngVel_array = DataFrame(AngVel_array)
        fullFile4 = pandas.concat([fullFile4, AngVel_array], join = 'inner')
