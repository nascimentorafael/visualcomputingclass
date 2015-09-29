import numpy as np

def passa_baixa9():
    
    filtro = np.ones((3,3), dtype="int8")
    
    div = 9
    
    return filtro, div

def passa_baixa25():
    
    filtro = np.ones((5,5), dtype="int8")
    
    div = 25
    
    return filtro, div
    
def filtro_media():
    filtro = np.ones((3,3), dtype="int8")
    
    div = 9
    
    return filtro, div