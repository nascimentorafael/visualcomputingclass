#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np
import Exercicio as e

    
def main():

    # LETRA A:
    # Aplicando negativos naslimagens:
    
    img1 = rw.readImage('imgs/img1.jpg',False)
    img1 = e.imagemNegativa(img1)
    rw.writeImage('imgs/img1-negativo.jpg',img1)
    
    img2 = rw.readImage('imgs/img2.jpg',False)
    img2 = e.imagemNegativa(img2)
    rw.writeImage('imgs/img2-negativo.jpg',img2)
    
    img3 = rw.readImage('imgs/img3.jpg',False)
    img3 = e.imagemNegativa(img3)
    rw.writeImage('imgs/img3-negativo.jpg',img3)
    
    # LETRA B
    # Mapeamento dos níveis de cinza de 0 a 255

    img = rw.readImage('imgs/img1.jpg',False)
    img255 = e.transformacaoLinear(img,0,255)
    rw.writeImage('imgs/img1-0a255.jpg',img255)
    
    # LETRA C
    # Mapeamento dos níveis de cinza de 100 a 200
    
    img = rw.readImage('imgs/img1.jpg',False)
    img1100 = e.transformacaoLinear(img,100,200)
    rw.writeImage('imgs/img1-100a200.jpg',img1100)
    
    img = rw.readImage('imgs/img2.jpg',False)
    img2100 = e.transformacaoLinear(img,100,200)
    rw.writeImage('imgs/img2-100a200.jpg',img2100)
    
    img = rw.readImage('imgs/img3.jpg',False)
    img3100 = e.transformacaoLinear(img,100,200)
    rw.writeImage('imgs/img3-100a200.jpg',img3100)
    
    
    # LETRA D
    # Construir o histograma das transformações
    
    img1 = rw.readImage('imgs/img1.jpg',False)
    img2 = rw.readImage('imgs/img2.jpg',False)
    img3 = rw.readImage('imgs/img3.jpg',False)
    img1100 = rw.readImage('imgs/img1-100a200.jpg',False)
    img2100 = rw.readImage('imgs/img2-100a200.jpg',False)
    img3100 = rw.readImage('imgs/img3-100a200.jpg',False)
    
    x = range(0,256)
    
    output_filename_img1 = 'hist_img1.jpg'
    output_filename_img2 = 'hist_img2.jpg'
    output_filename_img3 = 'hist_img3.jpg'
    output_filename_img1100 = 'hist_img1-100a200.jpg'
    output_filename_img2100 = 'hist_img2-100a200.jpg'
    output_filename_img3100 = 'hist_img3-100a200.jpg'
    
    histograma1 = hist.getHistogram(img1, 256)
    histograma2 = hist.getHistogram(img2, 256)
    histograma3 = hist.getHistogram(img3, 256)
    histograma1100 = hist.getHistogram(img1100, 256)
    histograma2100 = hist.getHistogram(img2100, 256)
    histograma3100 = hist.getHistogram(img3100, 256)
    
    config1 = {
    'filename': 'histogram/' + output_filename_img1,
    'title':u'Histograma:' + output_filename_img1,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    config2 = {
    'filename': 'histogram/' + output_filename_img2,
    'title':u'Histograma:' + output_filename_img2,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    config3 = {
    'filename': 'histogram/' + output_filename_img3,
    'title':u'Histograma:' + output_filename_img3,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    config1100 = {
    'filename': 'histogram/' + output_filename_img1100,
    'title':u'Histograma:' + output_filename_img1100,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    config2100 = {
    'filename': 'histogram/' + output_filename_img2100,
    'title':u'Histograma:' + output_filename_img2100,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    config3100 = {
    'filename': 'histogram/' + output_filename_img3100,
    'title':u'Histograma:' + output_filename_img3100,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    p1 = plot.plotgraph(x, histograma1, config1)
    p1.savePlot()
    
    p2 = plot.plotgraph(x, histograma2, config2)
    p2.savePlot()
    
    p3 = plot.plotgraph(x, histograma3, config3)
    p3.savePlot()
    
    p1100 = plot.plotgraph(x, histograma1100, config1100)
    p1100.savePlot()
    
    p2100 = plot.plotgraph(x, histograma2100, config2100)
    p2100.savePlot()
    
    p3100 = plot.plotgraph(x, histograma3100, config3100)
    p3100.savePlot()
    
    
    
if __name__ == '__main__':
    main()
    