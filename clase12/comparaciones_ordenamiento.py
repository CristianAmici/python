import random
import numpy as np
import matplotlib.pyplot as plt
def generar_lista(N):
    lista = [random.randint(0, 1000) for i in range(N)]
    return lista

def ord_burbujeo(lista):
  contador=1
  for i in range(1, len(lista)):
         for j in range(0, len(lista) - i):
             contador+=1
             if lista[j] > lista[j + 1]:
                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
  return contador
#%%
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador=0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
           contador=reubicar(lista, i + 1,contador)
            

    return contador

def reubicar(lista, p,contador):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    contador+=1
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        contador+=1
    lista[j] = v
    return contador
#%%
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    contador=1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        contador+=n-0
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        
        # reducir el segmento en 1
        n = n - 1

    return contador

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
def merge_sort(lista, contador=0):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, contador = merge_sort(lista[:medio],contador)
        der, contador = merge_sort(lista[medio:],contador)
        lista_nueva, contador = merge(izq, der,contador)
    return lista_nueva, contador

def merge(lista1, lista2,contador):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    contador+=1
    while(i < len(lista1) and j < len(lista2)):
        contador+=1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]
    return resultado, contador
#%%
def experimento(N, K):
    contador1=[]
    contador2=[]
    contador3=[]
    for i in range(K):
        lista=generar_lista(N)
        contador1.append(ord_burbujeo(lista.copy()))
        contador2.append(ord_insercion(lista.copy()))
        contador3.append(ord_seleccion(lista.copy()))
    contador1=np.array(contador1)
    contador2=np.array(contador2)
    contador3=np.array(contador3)
    tupla=(contador1.mean(),contador2.mean(),contador3.mean())
    return tupla
#%%
def experimento_vectores(Nmax):
    comparaciones_burbujeo=[]
    comparaciones_insercion=[]
    comparaciones_seleccion=[]
    comparaciones_mergeSort=[]
    for i in range(Nmax):
        lista=generar_lista(i)
        contador1=ord_burbujeo(lista.copy())
        contador2=ord_insercion(lista.copy())
        contador3=ord_seleccion(lista.copy())
        contador4=merge_sort(lista.copy())[1]
        comparaciones_burbujeo.append(contador1)
        comparaciones_insercion.append(contador2)
        comparaciones_seleccion.append(contador3)
        comparaciones_mergeSort.append(contador4)
    y1 = np.array(comparaciones_burbujeo)
    y2 = np.array(comparaciones_insercion)
    y3 = np.array(comparaciones_seleccion)
    y4= np.array(comparaciones_mergeSort)
    x = np.arange(0,Nmax)
    plt.plot(x,y1,color="r",label = 'Búsqueda Secuencial')
    plt.plot(x,y2,color='g',label="insercion")
    plt.plot(x,y3,color="b",label="seleccion")
    plt.plot(x,y4,color="y",label="Sort")
    plt.xlabel('Largo de la lista')
    plt.ylabel('Cantidad de Comparaciones')
    plt.title('experimento_vectores')
    plt.show()
#%%
experimento_vectores(300)
