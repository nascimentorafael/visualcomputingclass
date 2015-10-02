#coding=utf8
import lib.readwrite as rw
import lib.plotgraph as plot
import lib.histogram as hist
import numpy as np

    
def main():
    
    img = rw.readImage('../images/lena2.png',False)
    
    x = range(0,256)
    
    output_filename = 'hist_lena.png'
    
    histograma = hist.getHistogram(img, 256)
    
    config = {
    'filename': '../histogram/' + output_filename,
    'title':u'Histograma:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    img = rw.readImage('../images/lena2.png',False)
    
    x = range(0,256)
    
    output_filename = 'hist_lena_ac.png'
    
    histograma = hist.getHistogramAc(img, 256)
    
    config = {
    'filename': '../histogram/' + output_filename,
    'title':u'Histograma:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    img = rw.readImage('../images/lena2.png',False)
    
    x = range(0,256)
    
    output_filename = 'hist_lena_prob.png'
    
    histograma = hist.getHistogramProb(img, 256)
    
    config = {
    'filename': '../histogram/' + output_filename,
    'title':u'Histograma:' + output_filename,
    'xlabel':u'Nível de Cinza',
    'ylabel':u'Frequência',
    'color': 'grey',
    'alpha': 0.5,
    'grid': 'on',
    'xlimit': [0,255],
    }
    
    p = plot.plotgraph(x, histograma, config)
    p.savePlot()
    
    
    
if __name__ == '__main__':
    main()
    