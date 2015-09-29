#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np
from math import sqrt

# Gera uma imagem equalizada
def getImagemEqualizada(image, limit):
    his, a = np.histogram(image, limit)
    his = his.astype(float)/sum(his)
    
    return np.interp(image, a[1:], np.cumsum(his))

# Gera RMSE sobre duas imagens
def rmse(imageA, imageB):
	mse = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	mse /= float(imageA.shape[0] * imageA.shape[1])
	rmse =  sqrt(mse)
	
	return rmse

def main():
    
    # Gerar a imagem equalizada da imagem 'aereo.png'
    
    img = rw.readImage('img/aereo.png',False)
    imgEqualizada = getImagemEqualizada(img, 256)
    rw.writeImage("img_equalizada/aereo_equalizado.png", imgEqualizada)
    
    
    
    # Gera a imagem equalizada da imagem 'placa.jpg'
    
    img = rw.readImage('img/placa.jpg',False)
    imgEqualizada = getImagemEqualizada(img, 256)
    rw.writeImage("img_equalizada/placa_equalizado.jpg", imgEqualizada)
    
    
    
    # Gera a imagem equalizada da imagem 'daenarys_modificada.jpg'
    
    img = rw.readImage('img/daenarys_modificada.jpeg',False)
    imgEqualizada = getImagemEqualizada(img, 256)
    rw.writeImage("img_equalizada/daenarys_modificada_equalizado.jpeg", imgEqualizada)
    
    
    
    # Gera a imagem equalizada da imagem 'lena_modificada.jpg'
    
    img = rw.readImage('img/lena_modificada.png',False)
    imgEqualizada = getImagemEqualizada(img, 256)
    rw.writeImage("img_equalizada/lena_modificada_equalizado.png", imgEqualizada)
    
    
    
    # Gera o histograma da imagem 'aereo.png' original
    
    img = rw.readImage('img/aereo.png',False)
    x = range(0,256)
    output_filename = 'hist_aereo.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram/' + output_filename,
    'title':u'Histograma da imagem aereo.png original:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'gray',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'placa.jpg' original
    
    img = rw.readImage('img/placa.jpg',False)
    x = range(0,256)
    output_filename = 'hist_placa.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram/' + output_filename,
    'title':u'Histograma da imagem placa.jpg original:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'gray',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'daenarys_modificada.jpeg' original (sem equalização)
    
    img = rw.readImage('img/daenarys_modificada.jpeg',False)
    x = range(0,256)
    output_filename = 'hist_placa_daenarys_modificada.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram/' + output_filename,
    'title':u'Histograma da imagem daenarys_modificada.jpg original (sem equalização):' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'gray',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'lena_modificada.png' original (sem equalização)
    
    img = rw.readImage('img/lena_modificada.png',False)
    x = range(0,256)
    output_filename = 'hist_placa_lena_modificada.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram/' + output_filename,
    'title':u'Histograma da imagem lena_modificada.png original (sem equalização):' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'gray',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'aereo.png' equalizada
    
    img = rw.readImage('img_equalizada/aereo_equalizado.png',False)
    x = range(0,256)
    output_filename = 'hist_aereo_equalizado.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram_equalizado/' + output_filename,
    'title':u'Histograma da imagem aereo.png equalizada:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'red',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'placa.png' equalizada
    
    img = rw.readImage('img_equalizada/placa_equalizado.jpg',False)
    x = range(0,256)
    output_filename = 'hist_placa_equalizado.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram_equalizado/' + output_filename,
    'title':u'Histograma da imagem placa.jpg equalizada:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'red',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'daenerys_modificada_equalizada.jpeg' equalizada
    
    img = rw.readImage('img_equalizada/daenarys_modificada_equalizado.jpeg',False)
    x = range(0,256)
    output_filename = 'hist_daenerys_modificada_equalizado.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram_equalizado/' + output_filename,
    'title':u'Histograma da imagem daenerys_modificada_equalizada.jpeg equalizada:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'red',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # Gera o histograma da imagem 'lena_modificada_equalizada.png' equalizada
    
    img = rw.readImage('img_equalizada/lena_modificada_equalizado.png',False)
    x = range(0,256)
    output_filename = 'hist_lena_modificada_equalizado.png'
    histograma = hist.getHistogram(img, 256)
    config = {
    'filename': 'histogram_equalizado/' + output_filename,
    'title':u'Histograma da imagem lena_modificada_equalizada.png equalizada:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'red',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
    # RMSE: comparando 'daenarys_original.jpg' com 'daenarys_modificada_equalizado.jpeg'
    im1 = rw.readImage('img/daenarys_original.jpg',False)
    im2 = rw.readImage('img_equalizada/daenarys_modificada_equalizado.jpeg',False)
    err = rmse(im1, im2)
    # Imprime o rmse
    print("RMSE-daenarys: ",err)
    
    
    
    # RMSE: comparando 'lena_original.png' com 'lena_modificada_equalizado.png'
    im1 = rw.readImage('img/lena_original.png',False)
    im2 = rw.readImage('img_equalizada/lena_modificada_equalizado.png',False)
    err = rmse(im1, im2)
    # Imprime o rmse
    print("RMSE-lena: ",err)
    
    

if __name__ == '__main__':
    main()