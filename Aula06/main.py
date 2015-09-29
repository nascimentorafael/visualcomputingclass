#coding=utf8
import numpy as np
import lib.readwrite as rw
import lib.filtros as f


def correlacao(imagem, filtro, div_value):
    m = filtro.shape[0]
    n = filtro.shape[1]

    M = imagem.shape[0]
    N = imagem.shape[1]

    newimage = np.zeros((N,M),dtype="int8")

    mask_size = m

    alpha = np.int(np.ceil(mask_size/2))

    for i in range(alpha, M-alpha):
        for j in range(alpha,N-alpha):
            subimage = slice(imagem, i, j, mask_size)
            result = filtro * subimage
            soma = np.sum(result)/div_value

            if (soma < 0):
                soma = 0
            if (soma > 255):
                soma = 255

            newimage[i,j] = np.uint8(soma)
            
    return newimage

def slice(image, x, y, size):
        alpha = np.ceil(size/2)
        return image[x-alpha:x+(alpha+1):1,y-alpha:y+(alpha+1):1]


def main():
        imagem = rw.readImage("../images/lena2.png", True)
        filtro, div = f.passa_baixa()
        new1 = correlacao(imagem,filtro,div)
        rw.writeImage("../images/lena-filtro.png", new1)
        print("hi")
    
if __name__ == '__main__':
        main()