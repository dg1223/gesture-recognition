# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 22:28:29 2015

@author: Shamir
"""

import pandas
import os
import numpy as np
from natsort import natsorted
from pandas import DataFrame
from scipy.spatial.distance import euclidean

source_left = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Left_combined\\'                       # source folder
source_right = 'C:\\Users\\Shamir\\Desktop\\Hands_Sorted\\Right_combined\\'                                      # naturally sort the file list
destination_left  =  'C:\\Users\\Shamir\\Desktop\\Features\\Left\\'             # gestures performed only with the left hand go here
destination_right =  'C:\\Users\\Shamir\\Desktop\\Features\\Right\\'            # gestures performed only with the right hand go here
fileformat = '.csv'

def Convert2Euclidean(sourcePath, destinationPath):
    
    count = 1
    filelist = os.listdir(sourcePath)
    filelist = natsorted(filelist)
    for file in range(len(filelist)):
        
        alpha = ['alpha']
        beta =  ['beta']
        gamma = ['gamma']
        alpha = np.asarray(alpha)
        beta = np.asarray(beta)
        gamma = np.asarray(gamma)
        
        for i in range(1, number_of_rows):
            for j in range(0, number_of_columns, 4):
                
                secondIndex = j + 1
                thirdIndex  = j + 2
                fourthIndex = j + 3
                
                qr = sourceFile.values[i, j]
                qx = sourceFile.values[i, secondIndex]
                qy = sourceFile.values[i, thirdIndex]
                qz = sourceFile.values[i, fourthIndex]
                
                Alpha = np.arctan((2*(qr*qx + qy*qz)) / (1 - 2*(np.square(qx) + np.square(qy)))) * 180/np.pi
                Beta  = np.arcsin(2*(qr*qy - qx*qz))                                             * 180/np.pi
                Gamma = np.arctan((2*(qr*qz + qx*qy)) / (1 - 2*(np.square(qy) + np.square(qz)))) * 180/np.pi
                
                alpha = 