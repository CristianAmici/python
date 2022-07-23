#%%
def buscar_u_elemento(lista, elemento):
    pos=-1
    for index,numero in enumerate(lista):
        
        if numero==elemento:
            pos=index
    return pos

lista=[1,2,5,2,3,4]
print(buscar_u_elemento(lista,1))
print(buscar_u_elemento(lista,2))
print(buscar_u_elemento(lista,3))
print(buscar_u_elemento(lista,5))
#%%
def buscar_n_elementos(lista, elemento):
    
    n=0
    for numero in lista:
        if numero==elemento:
            n=n+1
    return n
lista=[1,2,5,2,3,4]
print(buscar_n_elementos(lista,1))
print(buscar_n_elementos(lista,2))
print(buscar_n_elementos(lista,3))
print(buscar_n_elementos(lista,5))
#%%
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e>m:
            m=e
    return m
lista=[1,2,5,2,3,4]
print(maximo(lista))
#%%
def minimo(lista):
    '''Devuelve el minimo de una lista'''
    # m guarda el minimo de los elementos a medida que recorro la lista. 
    m = 0 # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e<m:
            m=e
    return m
#%%
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos
#%%
def busqueda_lineal_lordenada(lista,e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        elif z>e:
            break
    return pos
#%%
def main():
    lista=[1,2,5,2,3,4]
    print(minimo(lista))
#main()