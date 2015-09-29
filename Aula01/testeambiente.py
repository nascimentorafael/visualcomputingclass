from scipy import misc

lena = misc.lena()

misc.imsave("../images/lena.png",lena)

img = misc.imread("../images/lena.png")

print type(lena)

print lena.shape