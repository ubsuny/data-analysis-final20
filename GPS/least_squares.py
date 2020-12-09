import numpy as np

def least_squares(ds, t, n = 2):
    
    # To generalize it for higher dimensions, but not necessary
    T = np.zeros((ds.shape[0], n + 1))
    
    # Add each iteration of t^n
    for idx in range(n + 1):
        T[:,idx] = t**idx
    
    # As defined in Theory.
    A = T.T @ T
    b = T.T @ ds
    
    return np.linalg.solve(A, b)

def chi2(actual, predicted, std):
    # The difference of the actual and predicted data
    difference = actual - predicted

    # Accounting for standard deviation
    division = difference/std

    # Returning the value of chi2
    return np.sum(division**2)

def rmse(actual, predicted, std):
    # chi2.
    goodness_of_fit = chi2(actual, predicted, std)

    # Returning the value of rmse.
    return np.sqrt(goodness_of_fit/actual.shape[0])