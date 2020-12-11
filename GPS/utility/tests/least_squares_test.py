# So we can access the utility files:
import sys
sys.path.append('../')

import numpy as np

# The main library:
from least_squares import least_squares, chi2, rmse

# The test:
def test_least_squares():
    # First, we can test in the base case where it's a polynomial of the form
    x = np.linspace(0, 10, 1000)
    y = x**2

    # Due to all of the multiplication going on, the constants might not 
    # properly zero out.  This is ok because we know that they should be zero.
    coefficients = np.round(least_squares(y, x), decimals = 10)
    
    # Coefficients are ordered by increasing power
    assert(coefficients[0] == 0)
    assert(coefficients[1] == 0)
    assert(coefficients[2] == 1)

    # Then, chi2.  This should be less than 1e-10 since we rounded by that decimal.

    f = coefficients[0] + coefficients[1]*x + coefficients[2]*x**2

    # We introduce neglible STD so that we know that our results are consistent.  
    assert(chi2(y, f, 1) < 1e-10)

    # RMSE as well.  But this should be sqrt(1e-10/1000)  
    assert(rmse(y, f, 1) < np.sqrt(1e-10/1000))

    # We can also do the linear case for the equation y = 5x + 10
    y = 5*x + 10

    coefficients = np.round(least_squares(y, x), decimals = 10)
    
    # This test is good because it shows that if you overshoot with the degree
    # least-squares will still return the lesser polynomial.
    # Coefficients are ordered by increasing power
    assert(coefficients[0] == 10)
    assert(coefficients[1] == 5)
    assert(coefficients[2] == 0)

    # And if we perturb the data a bit we can show that the error increases.
    x_p = x + np.random.choice(np.linspace(-0.1, 0.1, 1000))

    coefficients_p = np.round(least_squares(y, x_p), decimals = 10)
    
    f = coefficients[0] + coefficients[1]*x + coefficients[2]*x**2
    f_p = coefficients_p[0] + coefficients_p[1]*x + coefficients_p[2]*x**2

    assert(chi2(y, f, 1) < chi2(y, f_p, 1))

    # We don't have to worry about the case where 
    # x_0 = x_1 = x_2 = ... x_P because 
    # Vandermonde matrices force away singularity. 
