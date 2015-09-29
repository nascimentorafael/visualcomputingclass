#coding=utf8
#filename: readwrite.py

import scipy.misc
from scipy.misc.pilutil import Image


def readImage(path_image, convert):
    if (convert):
        im = Image.open(path_image).convert('L')
    else:
        im = Image.open(path_image)
    
    im = scipy.misc.fromimage(im)
    
    return im

def writeImage(path_image,numpy_image):
    c = scipy.misc.toimage(numpy_image)
    c.save(path_image)
