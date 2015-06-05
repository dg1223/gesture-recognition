import pandas
import numpy as np
import os

gesture_path = 'C:\\Users\\Shamir\\Desktop\\Grad\\Gesture Stuff\\Data_Multisensor\\'
gesture_list = os.listdir((gesture_path))               # '1. Jab\\2. Uppercut\\3.Throw\\4. Jets\\5. Block\\6. Asgard\\'
dataset_list = os.listdir((gesture_list))
files_list =                       # datasets

count = 0
for i in range(len(os.listdir(gesture_path))):        # we have 6 files corresponding to 6 gestures
    gesture = os.listdir(gesture_path)[i]
    for j in range(len(dataset_list)):                  # we have 3 files corresponding to 3 datasets (train, cross-validation, test)
        dataset = os.listgesture_path + gesture + os.listdir()
        for k in range(len(files_list)):                # we have 5 sensors (15,16,17,18,19) 
            csvfile = gesture_path + gesture + dataset + files_list

csvfile = 'C:\\Users\\Shamir\\Desktop\\Grad\\Gesture Stuff\\Data_Multisensor\\1. Jab\\1. Train\\sensor15_jab.csv'
file1 = pandas.read_csv(csvfile, header = None)

array = file1.loc[:,range(0,file1.shape[1],5)]
    
    