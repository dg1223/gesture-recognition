import pandas

class DataReader(object):
    """It reads the data, combines columns that gave identical headings and writes the processed data to a CSV file.
       It also asks the user to specify the filepath where the datafiles or desired folders can be found.
    
    columns include:
        qr, qx, qy, qz and time
        qr: scalar element of the quaternion
        qx,qy,qz: vector elements of the quaternion
        time: timestamp (this class does not deal with timestamps)
    """
    userInput = input('Enter the full folder path for : ')   # add an exception block if the files are not found there
    
    def _init_(self):

    def readCSV(self):
        
        csvfile = 'C:\\Users\\shamiralavi\\Documents\\Data_Multisensor\\1. Jab\\new position\\run 2 (final)\\sensor15_jab.csv'
        file1 = pandas.read_csv(csvfile)