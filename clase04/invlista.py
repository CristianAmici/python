def invertir_lista(lista):
    invertida = []
    index=len(lista)-1
    for e in lista: # Recorro la lista
        invertida.append(lista[index])
        index=index-1
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))
print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))