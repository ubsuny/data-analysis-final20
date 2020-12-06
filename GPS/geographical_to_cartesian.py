import numpy as np


# The information for the conversions comes from:
# https://vvvv.org/blog/polar-spherical-and-geographic-coordinates

def convert_coordinates(latitude, longitude, altitude):

    # z coordinate in meters. 
    # np.array() is there in case the data is input as a Python list.
    z = np.array(altitude)

    # Latitude angle in radians (for sinusoidal funcs)
    rad_lat = np.array(latitude)*np.pi/180

    # Longitude angle in radians.
    rad_long = np.array(longitude)*np.pi/180

    # Radius, from z = rsin(lat)
    r = z/np.sin(rad_lat)

    # x, from x = rcos(lat)cos(long)
    x = r*np.cos(rad_lat)*np.cos(rad_long)

    # y, from y = rcos(lat)sin(long)
    y = r*np.cos(rad_lat)*np.sin(rad_long)

    # Once again, so the user doesn't have to figure out which entry is what arbitrarily.
    # All values in meters.
    cartesian_coordinates = {'x': x, 'y': y, 'z': z}

    return cartesian_coordinates