#coding=utf-8
import numpy as np
import lib.readwrite as rw

image1 = rw.readImage('../images/ruido1.jpg',True)
image2 = rw.readImage('../images/ruido2.jpg',True)
image3 = rw.readImage('../images/ruido3.jpg',True)

M = image1.shape[0]
N = image2.shape[1]

final_image = np.zeros((M,N), dtype = 'uint8')

for i in range(0,M):
    for j in range(0,N):
        
        value = np.uint16(image1[i,j]) + np.uint16(image2[i,j]) + np.uint16(image3[i,j])
        final_image[i,j]  = np.uint8(value/3)

rw.writeImage('../images/ruidofinal.jpg',final_image)