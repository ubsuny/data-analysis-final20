# compute parameters of the fitting equation and chi square

import numpy as np

def fit(time,data,n):
    
    '''
     Fit for circular motion with a constant acceleration.
     Input: time is the absolute time, data is the actual data points, n is the order of the fitting function.
     Data does not include uncertainty.
    '''
    
    # define matrix A, Y
    n += 1
    Y = np.arange(n)
    A = np.zeros((time.shape[0],Y.shape[0]))
    
    # fill the matrix A
    for i in Y:
        A[:,i] = time ** i
        
    # construct left and right hand side of the equation
    left = A.T @ A
    right = A.T @ data
    
    # use numpy to compute parameter set a
    a = np.linalg.solve(left,right)
    
    return a

def func (time, para):
    '''
    Get the fitting values.
    Input: time is measured time data while para is parameters for the fitting function.
    '''
    n = para.shape[0]

    # the first parameter should be a constant
    f = para[0]

    # fill the function
    for i in np.arange(1,n):
        f = f + para[i] * (time**i)
        
    return f

def chi2 (data,fit,m):
    '''
    Compute chi square and the variance.
    Input: data is the actual data points and fit is the fitting points;
    and m here means the number of constraints.
    Since the uncertainty of data is always considered as 1 so chi2 is the mean-squared distance.
    '''
    
    # calculate the chi square
    chi2 = np.sum((data-fit)**2)
    
    # calculate the variance
    dof = data.shape[0]
    var = chi2 / (dof - m)
    
    return chi2, var