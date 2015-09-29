#coding=utf8

import scipy.misc
from scipy.misc.pilutil import Image

im = Image.open ('../images/lena.png').convert('L')

im = scipy.misc.fromimage(im)

b = im

c = scipy.misc.toimage(b)

c.save('../images/lena2.png')