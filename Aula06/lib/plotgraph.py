#coding=utf8

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 

class plotgraph():
    
    def __init__(self, x, data,config=None):
        self.x = x
        self.data = data
        self.config = config
        
    def savePlot(self):
        if(self.config is not None):
            plt.xlabel(self.config['xlabel'])
            plt.ylabel(self.config['ylabel'])
            plt.title(self.config['title'])
            plt.grid(self.config['grid'])
            plt.subplot().set_xlim(self.config['xlimit']) 
        
        
        

        plt.bar(self.x, self.data,color=self.config['color'],alpha=self.config['alpha'],align="center")
        plt.savefig(self.config['filename'])
        plt.close()
        