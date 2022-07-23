import numpy as np
import random 
#%%
def resumen_temp(n):
    lista= medir_temp(n)
    maximo= round(max(lista),2)
    minimo= round(min(lista),2)
    promedio= round(sum(lista)/n,2)
    lista.sort()
    media= lista[int(round(len(lista)/2+1,0))]
    return(maximo,minimo,promedio,media)
#%%
def medir_temp(n):
    lista=[]
    for i in range(n):
        lista.append(random.normalvariate(37.5, 0.2))
    guardado=np.array(lista)
    np.savetxt('../Data/temperaturas.npy',guardado)
    return lista
#%%
print(resumen_temp(999))