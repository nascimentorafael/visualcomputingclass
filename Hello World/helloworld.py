#Using scipy to handle image processing
from scipy import misc

# Using lena as a test
# Lena is the hello world from scipy
lena = misc.lena()

# Save lena
misc.imsave("../images/lena.png",lena)

# Read image lena form images folder
img = misc.imread("../images/lena.png")

print type(lena)

# Print image shape (512, 512)
print lena.shape