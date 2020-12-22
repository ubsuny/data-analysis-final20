def peakfinder(data, time, xbin):
    peaks = []
    for i in range(len(time)-1):
        if data[i]>data[i+1] and data[i]>data[i-1] and data[i]>data[i+xbin] and data[i]>data[i-xbin]:
            peaks.append(data[i])
    indx = []
    for i in range(len(data)):
        if data[i] in peaks:
            indx.append(i)
    return peaks, indx
'''
 This simple peakfinder algorithm works on sufficiently smoothed data, although 
 parameters can be altered to make it work for different data sets.
 The rather cumbersome "if" condition finds all local maxima, and then filters
 for maxima within the set bin, which can be chosen by eyeballing data to figure out 
 which peaks are statistically significant and estimating the necessary width.
 
 Returns: peaks: peak values, indx: peak indices
 
 '''