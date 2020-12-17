from read_data import *
from fitting import *

# test the read_data file
def test_read_data():
    # test the wrong path result
    wrong = read_data('nowhere.csv')
    assert not wrong
    
    # test correct path result, only valid for a gyroscope csv file
    # since they're a always 5 * n numpy array 
    gyroresult = read_data('../data/Raw Data_12_12.csv')
    n = gyroresult.shape
    assert n[0] == 5
    

# test the fit, func and chi2 function
def test_fit():
    '''
    we need to design specifically arrays to check the fit function and chi2 value 
    x is from 1 to 10 as an independent variable
    yexa is the exact result after squaring x
    ydata is the "measured" result, which is close to yact but with a standard deviation of 1
    '''
    x = np.arange(1,11)
    yexa = x ** 2
    ydata = 1 * np.random.randn(10) + yexa  
    
    # get and check fitting function parameters
    exapara = fit(x,yexa,2)
    fitpara = fit(x,ydata,2)
    # check the length of the return parameter list
    assert len(exapara) == 3.0
    assert len(fitpara) == 3.0 
    # check the first parameter (lowest order term), the exact set should always be zero 
    dif = abs(fitpara[0]) - abs(exapara[0])
    assert dif > 0.0
    
    # get the fitting points
    yfitexa = func(x,exapara)
    yfitdata = func(x,fitpara)
    # check the shape
    assert yfitexa.shape == x.shape and yfitdata.shape == x.shape

    # get chi2 and variance 
    chi2exa = chi2(yexa,yfitexa,2)
    chi2data = chi2(ydata,yfitdata,2)
    # chi2 of the exact set should be zero since it's perfect fitted
    assert chi2exa[0] < chi2data[0]


test_fit()
test_read_data() 