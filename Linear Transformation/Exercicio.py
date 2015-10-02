#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np

def imagemNegativa(image):
    img = -1 * image + 255
    return img
  
    
def transformacaoLinear(image, g_min,g_max):
    M = image.shape[0]
    N = image.shape[1]
    
    f_max = max(image.flatten())
    f_min = min(image.flatten())
    
    for i in range(0,M):
        for j in range(0,N):
            image[i,j] = funcaoLinear(image[i,j],f_max,f_min,g_max,g_min)
    
    return image

def funcaoLinear(v_pixel,f_max,f_min,g_max,g_min):

    a = float((g_max - g_min))/(f_max - f_min)
    b = g_min
    f = (v_pixel - f_min)
    
    g = (a*f) + b
    
    return g
    