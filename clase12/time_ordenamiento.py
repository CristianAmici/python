import random
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt
def generar_lista(N):
    lista = [random.randint(0, 1000) for i in range(N)]
    return lista
#%%
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))

# tiempos_ordenamiento = experimento_timeit(listas, 100)
# plt.plot(tiempos_ordenamiento)
#%%
def experimento_timeit(Nmax):
     tiempos_burbujeo = []
     tiempos_insercion = []
     tiempos_seleccion = []
     tiempos_mergeSort= []
     global lista
     for i in range(Nmax):
        lista=generar_lista(i)
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = 1, setup="from time_ordenamiento import ord_burbujeo",  globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = 1, setup="from time_ordenamiento import ord_insercion", globals = globals())
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = 1, setup="from time_ordenamiento import ord_seleccion", globals = globals())
        tiempo_mergeSort = tt.timeit('merge_sort(lista.copy())', number = 1, setup="from time_ordenamiento import merge_sort", globals = globals())
        # guardo el resultado
        tiempos_burbujeo.append(tiempo_burbujeo)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_mergeSort.append(tiempo_mergeSort)
     y1 = np.array(tiempos_burbujeo)
     y2 = np.array(tiempos_insercion)
     y3 = np.array(tiempos_seleccion)
     y4= np.array(tiempos_mergeSort)
     x = np.arange(0,Nmax)
     plt.plot(x,y1,color="r", label = "burbujeo")
     plt.plot(x,y2,color='g', label = "insercion")
     plt.plot(x,y3,color="b", label = "seleccion")
     plt.plot(x,y4,color="y", label = "Sort")
     plt.xlabel('Largo de la lista')
     plt.ylabel('Tiempo que tarda')
     plt.title('Largo de la lista')
     plt.show()
#%%    
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        
        # reducir el segmento en 1
        n = n - 1

    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
#%%
def ord_burbujeo(lista):
    
    tamano=len(lista)
    comparaciones=tamano
    for i in range(0,tamano):
        for j in range(0,comparaciones-1):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
        comparaciones=comparaciones-1
    return lista
#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
           lista=reubicar(lista, i + 1)
            

    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
    lista[j] = v
    return lista
#%%
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
   
    while(i < len(lista1) and j < len(lista2)):
    
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado
#%%
experimento_timeit(280)