import pandas as pds 
import numpy as np
import os

# TO-DO:  include os to check to make sure that the file exists.  this is a very basic unit test.  if exists, empty dict.  if not, full dict.
def get_data(filename):

    if os.path.exists(filename):
        # Open csv
        table = pds.read_csv(filename)

        # Remove values where there are zero satellites (data cannot be trusted)
        table = table[table['Satellites'] != 0.0]

        # Time
        time = np.array(table['Time (s)'])

        # Position variables in geographical coordinates
        latitude, longitude, altitude = np.array(table['Latitude (°)']), np.array(table['Longitude (°)']), np.array(table['Altitude (m)'])

        # Standard deviation.  Vertical is 'z' and horizontal is 'x' and 'y'.
        # Neither are the standard deviation for the geograhpical coordinates.
        std_vertical, std_horizontal = np.array(table['Vertical Accuracy (m)']), np.array(table['Horizontal Accuracy (m)'])

        # Position dictionary.  This is so any user doesn't necessarily need to read the code beyond the jupyter notebook.
        position = {'time': time, 'latitude': latitude, 'longitude': longitude, 'altitude': altitude, 'z std': std_vertical, 'x & y std': std_horizontal}
        
    else:
        print('file not found!')
        position = {}

    return position