# Paper
[Quaternion-Based Gesture Recognition Using Wireless Wearable Motion Capture Sensors ] (https://www.mdpi.com/1424-8220/16/5/605)

[Dataset] (https://www.mdpi.com/1424-8220/16/5/605/s1)

# ThesisCodes
Codes for my Master's Thesis

# Data Extraction and Conversion
Replace Missing Values.py - Replaces missing values for the Beta angle after conversion from quaternion to Euclidean.

add_headers.py - adds appropriate header columns to each dataset

columnSorter.py - breaks quaternion datasets in four different datasets that hold individual quaternion components

columnSorter_euclid.py - same as above but for datasets with Euclidean components

columnSorter_pStudy.py - same as above but for individual participant dataset

columnJoiner.py - joins every individual quaternion dataset to create a new dataset with homogenous quaternion component

convert2euclidean.py - convert quaternion components to Euclidean components

outlierRemover.py - removes outliers by applying linear interpolation using a 10-point sliding window

# Data Paritioning (not Train, Validation, Test)
sortLeftRight.py - separates the left and right-hand gestures and turns them into individual datasets

*Training, Validation and Test sets were created using Weka 3.6

# Feature Extraction
featureExtraction.py - Extracts five features from every dataset: Variance, Range, Velocity, Angular Velocity, Covariance

# Test Scripts
test.py, test2.py, test3.py, testFileSize.py, test_covariance.py, test_range.py, test_variance.py, test_velocity.py
*Each file has its own description

# Miscellaneous (just for fun!)
countDatapoints.py - counts the total number of datapoints in a dataset

# Data Preprocessing/Model Evaluation/Dimensionality Reduction/Feature Selection/Result Analysis
were done in Weka 3.6
