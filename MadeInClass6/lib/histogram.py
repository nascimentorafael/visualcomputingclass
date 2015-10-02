#coding=utf8

import numpy as np
import math

def getHistogram(image,limit):
    
    array = image.flatten()
    hist = np.zeros(limit,dtype='int')
    
    for i in range(0,len(array)):
        hist[array[i]] = hist[array[i]] + 1
        
    return hist
  
#def getHistogramProb(image, limit):
#    M = float(image, shape[0])
#    N = float(image, shape[0])
    
#    histograma = getHistogram(image,limit)
    
#   hist = np.zeros(limit, dtype='float64')
