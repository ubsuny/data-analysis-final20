import pandas as pds 
import numpy as np
import os

def get_data(filename, ignore_zeros = False):

    # Declare an empty position dictionary:
    position = {}

    # Declare the standard keys:
    keys = ['Time (s)', 'Latitude (°)', 'Longitude (°)', 'Altitude (m)',
       'Altitude WGS84 (m)', 'Speed (m/s)', 'Direction (°)', 'Distance (km)',
       'Horizontal Accuracy (m)', 'Vertical Accuracy (m)', 'Satellites']

    # Does the file even exist?
    if os.path.exists(filename):
        # Open csv
        table = pds.read_csv(filename)

        # Just because it's a csv doesn't mean that it's the data we need.
        if keys == list(table.keys()):
            
            if ignore_zeros == False:
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

    return position