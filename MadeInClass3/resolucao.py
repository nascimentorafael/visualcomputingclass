#coding=utf-8

import lib.readwrite as rw
import scipy.misc
import numpy as np
import vizinhaca as v

img = rw.readImage('../images/lena.png',False)

newimg = scipy.misc.imresize(img, (256,256))
rw.writeImage('../images/lena256x256.png',newimg)

newimg = scipy.misc.imresize(img, (128,128))
rw.writeImage('../images/lena128x128.png',newimg)

newimg = scipy.misc.imresize(img, (64,64))
rw.writeImage('../images/lena64x64.png',newimg)

newimg = scipy.misc.imresize(img, (32,32))
rw.writeImage('../images/lena32x32.png',newimg)

newimg = scipy.misc.imresize(img, (16,16))
rw.writeImage('../images/lena16x16.png',newimg)

newimg = scipy.misc.imresize(img, (8,8))
rw.writeImage('../images/lena8x8.png',newimg)

img8p = rw.readImage('../images/lena8x8.png',False)

#v.print_vizinhaca(img8p)

#print(img8p)

imgc = rw.readImage('../images/b0.png',True)
print(imgc)

v.contorno(imgc)
rw.writeImage("../images/b1.png",imgc)

print (imgc)