import random
import matplotlib.pyplot as plt
import numpy as np
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        comps += 1 # sumo la comparaci�n que estoy por hacer
        if izq==der:
            pos=medio
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, comps
#%%
def donde_insertar(lista, x):
    pos= busqueda_binaria(lista,x)
    return pos
#%%
def insertar(lista, x):
    pos=donde_insertar(lista,x)[0]
    if lista[pos]==x:
        return pos
    else:
        lista.insert(pos, x)
        return pos
#%%
def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)
#%%
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%
def busqueda_secuencial_(lista, x):
    '''Si x est� en la lista devuelve el �ndice de su primera aparici�n, 
    de lo contrario devuelve -1. Adem�s devuelve la cantidad de comparaciones
    que hace la funci�n.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparaci�n que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps

#%%
def graficar_bbin_vs_bseq(m, k):
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_binario= np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)
    # ahora grafico largos de listas contra operaciones promedio de b�squeda.
    plt.plot(largos,comps_promedio_secuencial,label = 'B�squeda Secuencial')
    plt.plot(largos,comps_promedio_binario,label = 'B�squeda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la B�squeda")
    plt.legend()
    plt.show()
def main():
    m = 10000
    k = 1000
    graficar_bbin_vs_bseq(m,k)