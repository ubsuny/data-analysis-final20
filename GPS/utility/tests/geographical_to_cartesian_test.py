# So we can access the utility files:
import sys
sys.path.append('../')

import numpy as np

# The main library:
from geographical_to_cartesian import convert_coordinates

# The test:
def test_convert_coordinates():
    # First, a standard case.  No vectorization and
    # a simple expression of the coordinates.
    r, theta, phi = 1, 90, 0

    cartesian_coordinates = convert_coordinates(theta, phi, r)
    
    # First assert that it is is a dictionary:
    assert(type(cartesian_coordinates) == dict)

    # Then assert that the results are as expected:
    assert(round(cartesian_coordinates['x'], -16) == 0)
    assert(round(cartesian_coordinates['y'], -16) == 0)
    assert(cartesian_coordinates['z'] == r)

    # We can also vectorize the equations:
    rs = np.linspace(0, 1, 1000)

    vector_cartesian_coordinates = convert_coordinates(theta, phi, rs)

    # It's a bit arbitrary to check every value.  Instead, we can just check type:
    assert(type(vector_cartesian_coordinates['x']) == np.ndarray)