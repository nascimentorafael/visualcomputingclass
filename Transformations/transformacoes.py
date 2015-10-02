#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np
import math


def imagemNegativa(image):
    img = -1 * image + 255
    return img
    
    
def transformacaoLinear(image, g_min,g_max):
    M = image.shape[0]
    N = image.shape[1]
    
    f_max = max(image.flatten())
    f_min = min(image.flatten())
    
    for i in range(0,M):
        for j in range(0,M):
            image[i,j] = funcaoLinear(image[i,j],f_max,f_min,g_max,g_min)
    
    return image

def funcaoLinear(v_pixel,f_max,f_min,g_max,g_min):
    a = float((g_max - g_min))/(f_max - f_min)
    b = g_min
    f = (v_pixel - f_min)
    
    g = (a*f) + b
    
    return g
    
def transformacaoNaoLinearLog(image):
    M = image.shape[0]
    N = image.shape[1]
    
    f_max = max(image.flatten())
    f_min = min(image.flatten())
    
    for i in range(0,M):
        for j in range(0,N):
            image[i,j] = funcaoLog(image[i,j],f_max)
    
    return image
    
def transformacaoNaoLinearExpo(image):
    M = image.shape[0]
    N = image.shape[1]
    
    f_max = max(image.flatten())
    f_min = min(image.flatten())
    
    for i in range(0,N):
        for j in range(0,M):
            image[i,j] = funcaoExpo(image[i,j],f_max)
            
    return image
    
def funcaoLog(v_pixel,f_max):

    a = 255/math.log10(1+f_max)
    
    g = a * math.log10(v_pixel+1) 
    
    return g

def transformacaoNaoLinearQuadr(image):
    M = image.shape[0]
    N = image.shape[1]
    
    f_max = max(image.flatten())
    f_min = min(image.flatten())
    
    for i in range(0,M):
        for j in range(0,N):
            image[i,j] = funcaoQuadr(image[i,j],f_max)
    
    return image
    
def funcaoQuadr(v_pixel,f_max):

    a = 255/math.sqrt(f_max)
    
    g = a * math.sqrt(v_pixel) 
    
    return g
    
def funcaoExpo(v_pixel,f_max):
    
    a = 255 / (math.exp(f_max) - 1)
    
    g = a * (math.exp(v_pixel) - 1)
    
    return g


img = rw.readImage('../images/daenarys_escuro.jpeg',False)
imgLog = transformacaoNaoLinearLog(img)
rw.writeImage('../images/daenarys_escuro-log.jpeg',imgLog)

img = rw.readImage('../images/daenarys_escuro.jpeg',False)

imgQuadr = transformacaoNaoLinearQuadr(img)
rw.writeImage('../images/daenarys_escuro-quadr.jpeg',imgQuadr)

img = rw.readImage('../images/daenarys_escuro.jpeg',False)

x = range(0,256)

output_filename_img = 'hist_img_daenarys.jpeg'
output_filename_imglog = 'hist_img_daenarys-log.jpeg'
output_filename_imgquadr = 'hist_img_daenarys-quadr.jpeg'

histograma = hist.getHistogram(img, 256)
histogramalog = hist.getHistogram(imgLog, 256)
histogramaquadr = hist.getHistogram(imgQuadr, 256)

config = {
    'filename': '../images/' + output_filename_img,
    'title':u'Histograma:' + output_filename_img,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }

configlog = {
    'filename': '../images/' + output_filename_imglog,
    'title':u'Histograma:' + output_filename_imglog,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
configquadr = {
    'filename': '../images/' + output_filename_imgquadr,
    'title':u'Histograma:' + output_filename_imgquadr,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
p = plot.plotgraph(x, histograma, config)
p.savePlot()

plog = plot.plotgraph(x, histogramalog, configlog)
plog.savePlot()

pquadr = plot.plotgraph(x, histogramaquadr, configquadr)
pquadr.savePlot()
