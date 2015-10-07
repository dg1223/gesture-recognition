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