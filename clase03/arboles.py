def leer_parque(nombre_archivo, parque):
    import csv
    lista_arboles=[]
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        headers= next(filas)
        contador=0
        for fila in filas:
            try:
                record = dict(zip(headers, fila))
                if record['espacio_ve']==parque:
                    lista_arboles.append(record)
                    contador+=1
            except:
                print('...')
    return lista_arboles
   
def especies(lista_arboles):
    lista=[]
    for fila in lista_arboles:
       lista.append(fila['nombre_com'])
    
    
    unicos= set(lista)

    return unicos

def contar_ejemplares(lista_arboles):
    from collections import Counter
    diccionario= Counter()
    for fila in lista_arboles:
        diccionario[fila['nombre_com']]+=1
    return diccionario

def obtener_alturas(lista_arboles, especie):
    lista=[]
    for fila in lista_arboles:
        if fila['nombre_com']== especie:
            lista.append(float(fila['altura_tot']))
    
    return lista
def obtener_inclinaciones(lista_arboles, especie):
    lista=[]
    for fila in lista_arboles:
        if fila['nombre_com']== especie:
            lista.append(int(fila['inclinacio']))
    
    return lista
def especimen_mas_inclinado(lista_arboles):
    listaFinal={}
    inclinacion=0
    especiesAiterar= especies(lista_arboles)
    for especie in especiesAiterar:
        lista= obtener_inclinaciones(lista_arboles, especie)
        if inclinacion<max(lista):
            listaFinal={}
            inclinacion=max(lista)
            listaFinal[especie]=inclinacion
    return listaFinal
def especie_promedio_mas_inclinada(lista_arboles):
    import statistics
    listaFinal={}
    promedio=0
    especiesAiterar= especies(lista_arboles)
    for especie in especiesAiterar:
        lista= obtener_inclinaciones(lista_arboles, especie)
        if promedio<statistics.mean(lista):
            listaFinal={}
            promedio=statistics.mean(lista)
            listaFinal[especie]=promedio
    return listaFinal
parque=contar_ejemplares(leer_parque('../Data/arbolado_en_espacios_verdes.csv','GENERAL PAZ'))
print(parque.most_common(5))
parque=contar_ejemplares(leer_parque('../Data/arbolado_en_espacios_verdes.csv','ANDES, LOS'))
print(parque.most_common(5))
parque=contar_ejemplares(leer_parque('../Data/arbolado_en_espacios_verdes.csv','CENTENARIO'))
print(parque.most_common(5))

import statistics
parque=obtener_alturas(leer_parque('../Data/arbolado_en_espacios_verdes.csv','ANDES, LOS'),'Jacarandá')
print('maximo:' , max(parque), 'promedio:', statistics.mean(parque), 'Jacarandá en ANDES, LOS')
parque=obtener_alturas(leer_parque('../Data/arbolado_en_espacios_verdes.csv','CENTENARIO'),'Jacarandá')
print('maximo:' , max(parque), 'promedio:', statistics.mean(parque), 'Jacarandá en CENTENARIO')
parque=obtener_alturas(leer_parque('../Data/arbolado_en_espacios_verdes.csv','GENERAL PAZ'),'Jacarandá')
print('maximo:' , max(parque), 'promedio:', statistics.mean(parque), 'Jacarandá en GENERAL PAZ')

parque=especimen_mas_inclinado(leer_parque('../Data/arbolado_en_espacios_verdes.csv','GENERAL PAZ'))
print(parque)
parque=especimen_mas_inclinado(leer_parque('../Data/arbolado_en_espacios_verdes.csv','ANDES, LOS'))
print(parque)
parque=especimen_mas_inclinado(leer_parque('../Data/arbolado_en_espacios_verdes.csv','CENTENARIO'))
print(parque)
parque=especie_promedio_mas_inclinada(leer_parque('../Data/arbolado_en_espacios_verdes.csv','GENERAL PAZ'))
print(parque)
parque=especie_promedio_mas_inclinada(leer_parque('../Data/arbolado_en_espacios_verdes.csv','ANDES, LOS'))
print(parque)
parque=especie_promedio_mas_inclinada(leer_parque('../Data/arbolado_en_espacios_verdes.csv','CENTENARIO'))
print(parque)
print(leer_parque('../Data/arbolado_en_espacios_verdes.csv','GENERAL PAZ'))