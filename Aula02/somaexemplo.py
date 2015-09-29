#coding=utf-8

import time
from numpy import *

numtermos = 1000000

numeros = ones(numtermos)

soma1 = 0

t1 = time.clock()

for n in numeros:
    soma1 = soma1 + (n)

soma1 = soma1*4

t2 = time.clock()

print "Valor da soma %f" %soma1
print "Tempo %f"% (t2-t1)

print ''

t1 = time.clock()

soma2 = sum(numeros)*4.0

t2 = time.clock()

print "Valor da soma %f" %soma2
print "Tempo %f"% (t2-t1)