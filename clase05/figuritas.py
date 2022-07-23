import random
import numpy as np
#%%
def crear_album(figus_total):
      album=np.zeros(figus_total)
      return album
#%%
def album_incompleto(A):
    return 0 in A
#%%
def comprar_figu(figus_total):
    return random.randint(0,figus_total)
#%%
def cuantas_figus(figus_total):
    totalFiguritas=0;
    album=crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total-1)]=1
        totalFiguritas+=1
    return totalFiguritas
#%%
def experimento_figus(n_repeticiones, figus_total):
    lista= [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(lista)
print(experimento_figus(100,670))