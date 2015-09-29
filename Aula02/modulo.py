#coding=utf-8
import novomodulo
import lib.readwrite as rw

novomodulo.printpi() 

print ''

imagetest = rw.readImage('../images/lena.png',False)

b = imagetest

rw.writeImage('../images/lena3.png',b)

print imagetest
