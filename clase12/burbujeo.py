def ordenamiento_de_burbuja(lista):
   for i in range(1, len(lista)):
         for j in range(0, len(lista) - i):
             if lista[j] > lista[j + 1]:
                 lista[j], lista[j + 1] = lista[j + 1], lista[j]
   return lista

lista =  [10, 3, 5, 1, 6, 7, 6, 86, 32, 34, 78]
lista_ordenada = ordenamiento_de_burbuja(lista)

def iterador(n):
    for i in range (n):
        if i//2 ==i/2:
            yield i

pares= iterador(100)
lista=[]
for i in pares:
    lista.append(i)
print(lista_ordenada)