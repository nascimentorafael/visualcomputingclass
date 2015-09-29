#coding=utf8
import numpy as np

# Gera o histograma da imagem
def getHistogram(image,limit):
    
    imgArray = image.flatten()
    hist = np.zeros(limit,dtype='int')
    
    # Soma 1 para cada tom de cinza no histograma
    for i in range(0,len(imgArray)):
        hist[imgArray[i]] = hist[imgArray[i]] + 1
        
    return hist

# Gera o historama probabilidade  
def getHistogramProb(image, limit):
    
    M = float(image.shape[0])
    N = float(image.shape[1])
    
    histograma = getHistogram(image,limit)
    
    hist = np.zeros(limit, dtype='float64')
    
    for i in range (0, len(histograma)):
        hist[i] = histograma[i] / (M*N)
        
    return hist
    
# Gera o histograma acumulativo para a imagem
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
    
# Gera o histograma da probabilidade acumudala
def getHistogramProbAc(image, limit):
    histProb = getHistogramProb(image, limit)
    histAcc = np.cumsum(histProb)
    
    return histAcc