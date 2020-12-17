# read the csv files to get raw data

import pandas as pd
import numpy as np

def read_data(filename):
    
    '''
    Phyphox can output raw data as csv files. 
    For a gyroscope data, it has such format:
    time, gyroscope x, gyroscope y, gyroscope z, absolute value.
    '''

    try:
        # only if the file is found then start parsing

        file = pd.read_csv(filename)
        data = np.zeros((file.shape[1],file.shape[0]))
        
        data[0] = np.array(file['Time (s)'])
        data[1] = np.array(file['Gyroscope x (rad/s)'])
        data[2] = np.array(file['Gyroscope y (rad/s)'])
        data[3] = np.array(file['Gyroscope z (rad/s)'])
        data[4] = np.array(file['Absolute (rad/s)'])
        
        # return the data as a numpy array
        return(data)
    
    except:
        print("The file is not a csv file or it's not in the current folder.")
