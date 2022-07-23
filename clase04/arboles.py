def leer_arboles(nombre_archivo):
    #lo modifique para que reciba una lista con los arboles
    arboleda=[]
    filas = nombre_archivo
    headers=  [fila for fila in filas[0].keys()]
    indices = [ncolumna for ncolumna in headers]
    arboleda = [{ ncolumna: fila[index] for ncolumna, index in (zip(headers, indices))} for fila in filas]
    return arboleda

def leer_parque(nombre_archivo, parque):
    #Lo realice por parque para que no sea tan largo y maneje tantos datos
    #si no se selecciona el parque trae todos los arboles
    import csv
    lista_arboles=[]
    with open(nombre_archivo, encoding="utf8") as f:
        filas = csv.reader(f)
        headers= next(filas)
        contador=0
        for fila in filas:
            try:
                record = dict(zip(headers, fila))
                if record['espacio_ve']==parque or parque=='':
                    lista_arboles.append(record)
                    contador+=1
            except:
                print('...')
    return lista_arboles
def medidas_de_especies(especies,arboleda):
    H={clave: [(float(arbol['altura_tot']),arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==clave] for clave in especies }
    return H

arboleda=leer_arboles(leer_parque('../Data/arbolado_en_espacios_verdes.csv',''))
print(arboleda)
especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
H=medidas_de_especies(especies,arboleda)
print(len(H['Eucalipto']),len(H['Palo borracho rosado']),len(H['Jacarandá']))
H=[(float(arbol['altura_tot']),arbol['diametro']) for arbol in arboleda if arbol['nombre_gen']=='Jacarandá']
print(H)


