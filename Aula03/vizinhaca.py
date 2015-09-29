#coding=utf-8

def contorno(image):
    M = image.shape[0] #Numero de linhas da imagem
    N = image.shape[1] #Numero de colunas da imagem
    
    for i in range(0,M):
        for j in range(0,N):
            # Se o pixel é preto
            if image[i,j] == 0:
                # Verificar a vizinhaça 4
                v = [(_i,_j) for (_i,_j) in vizinhaca4(i,j) if image[_i,_j] == 255]
                
                for item in v:
                    image[i,j] = 128
                
            # Se algum dos elementos da vizinhaca 4 dele forem iguais a ele (preto), então ele é um contorno
            # Se ele é um contorno pintar ele de branco
    

def vizinhaca4(linha,coluna):
    v1 = (linha - 1, coluna)
    v2 = (linha, coluna - 1)
    v3 = (linha + 1, coluna)
    v4 = (linha, coluna + 1)
    
    return [v1,v2,v3,v4]
    
def vizinhaca8(linha, coluna):
    v5 = (linha - 1, coluna - 1)
    v6 = (linha - 1, coluna + 1)
    v7 = (linha + 1, coluna - 1)
    v8 = (linha + 1, coluna + 1)
    
    vizinhaca = vizinhaca4(linha, coluna) + [v5, v6, v7, v8]
    
    return vizinhaca
    
def print_vizinhaca(image):
    
    M = image.shape[0] #Numero de linhas da imagem
    N = image.shape[1] #Numero de colunas da imagem
    
    for i in range(0,M):
        for j in range(0,N):
            v = [(i,j) for (i,j) in vizinhaca4(i,j) if (i >= 0 and i < M) and (j >= 0 and j < N)]
            
            print "Vizinhaça " + str(i) + " " + str(j) + ":"
            
            for item in v:
                x = item [0]
                y = item [1]
                print image[x,y]
