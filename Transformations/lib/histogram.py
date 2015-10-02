#coding=utf8

import numpy as np
import math

def getHistogram(image,limit):
    
    array = image.flatten()
    hist = np.zeros(limit,dtype='int')
    
    for i in range(0,len(array)):
        hist[array[i]] = hist[array[i]] + 1
        
    return hist
  
def getHistogramProb(image, limit):
    
    M = float(image.shape[0])
    N = float(image.shape[1])
    
    histograma = getHistogram(image,limit)
    
    hist = np.zeros(limit, dtype='float64')
    
    for i in range (0, len(histograma)):
        hist[i] = histograma[i] / (M*N)
        
    return hist
    
# Histograma acumulativo para a imagem
def getHistogramAc(image, limit):
    M = float(image.shape[0])
    N = float(image.shape[1])
    
    histograma = getHistogram(image,limit)
    
    hist = np.zeros(limit, dtype='float64')
    
    acumulativo = 0
    
    for i in range (0, len(histograma)):
        hist[i] = histograma[i] + acumulativo
        acumulativo = acumulativo + histograma[i]
        
    return hist
