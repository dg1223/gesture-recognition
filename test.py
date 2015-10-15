# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 21:54:14 2015

@author: Shamir
"""

try:
                for k in range(num_columns):                
                    #print 'file = ', i, "row = ", j, "col = ", k
                    output_list.append(firstFile.loc [j, k])
                    output_list.append(secondFile.loc[j, k])
                    output_list.append(thirdFile.loc [j, k])
                    output_list.append(fourthFile.loc[j, k])
            except KeyError:
                #error = e.message[-26:-23]
                try:
                    num_columns = len(secondFile.values[0])
                    for k in range(num_columns):                
                        #print 'file = ', i, "row = ", j, "col = ", k
                        output_list.append(firstFile.loc [j, k])
                        output_list.append(secondFile.loc[j, k])
                        output_list.append(thirdFile.loc [j, k])
                        output_list.append(fourthFile.loc[j, k])
                except KeyError:
                    try:
                        num_columns = len(thirdFile.values[0])
                        for k in range(num_columns):                
                            #print 'file = ', i, "row = ", j, "col = ", k
                            output_list.append(firstFile.loc [j, k])
                            output_list.append(secondFile.loc[j, k])
                            output_list.append(thirdFile.loc [j, k])
                            output_list.append(fourthFile.loc[j, k])
                    except KeyError:
                        num_columns = len(fourthFile.values[0])
                        for k in range(num_columns):                
                            #print 'file = ', i, "row = ", j, "col = ", k
                            output_list.append(firstFile.loc [j, k])
                            output_list.append(secondFile.loc[j, k])
                            output_list.append(thirdFile.loc [j, k])
                            output_list.append(fourthFile.loc[j, k])
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
            except KeyError as e:
                if num_columns > 1000: 
                    error = int(e.message[-26:-22])
                    print 'columns > 1000 ', 'error value = ', error
                    num_columns = error
                    for k in range(num_columns):                
                        #print 'file = ', i, "row = ", j, "col = ", k
                        output_list.append(firstFile.loc [j, k])
                        output_list.append(secondFile.loc[j, k])
                        output_list.append(thirdFile.loc [j, k])
                        output_list.append(fourthFile.loc[j, k])
                else:
                    error = int(e.message[-26:-23])
                    print 'columns < 1000 ', 'error value = ', error
                    num_columns = error
                    for k in range(num_columns):                
                        #print 'file = ', i, "row = ", j, "col = ", k
                        output_list.append(firstFile.loc [j, k])
                        output_list.append(secondFile.loc[j, k])
                        output_list.append(thirdFile.loc [j, k])
                        output_list.append(fourthFile.loc[j, k])
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
    # Left Hand Gestures
    print 'Calculating LH Features'
    
    print 'Calculating variance'
    variance_l = Variance(source_left)
    
    print 'Calculating range'
    range_l    = Range(source_left)
    
    print 'Calculating velocity'
    velocity_l = Velocity(source_left)
    
    print 'Calculating angular velocity'
    AngVel_l   = AngularVelocity(source_left_Euclid)
    
    print 'Calculating covariance'
    covar_l    = Covariance(source_left)
    
    fullFile_l = pandas.concat([variance_l, range_l, velocity_l, AngVel_l, covar_l], axis = 1)
    fullFile_l.to_csv(destination + left + fileformat, header = False, index = False)
