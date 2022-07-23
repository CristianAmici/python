import os
import matplotlib.pyplot as plt
import numpy as np
#%%
def leer_arboles(nombre_archivo):
    #lo modifique para que reciba una lista con los arboles
    nombre_archivo=leer_parque(nombre_archivo, '')
    arboleda=[]
    filas = nombre_archivo
    headers=  [fila for fila in filas[0].keys()]
    indices = [ncolumna for ncolumna in headers]
    arboleda = [{ ncolumna: fila[index] for ncolumna, index in (zip(headers, indices))} for fila in filas]
    return arboleda
#%%
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
#%%
def medidas_de_especies(especies,arboleda):
    H={clave: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==clave] for clave in especies }
    return H
#%%
def scatter_hd(lista_de_pares):
    
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto de los arboles")
    for x,y in lista_de_pares:
        plt.scatter(x, y,s=20, c=60, alpha=0.5) 
    plt.show()
        
#%%
def grafico_jacarandá():
    arboleda=leer_arboles('../Data/arbolado_en_espacios_verdes.csv')
    especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas=medidas_de_especies(especies,arboleda)
    lista_de_pares=np.array(medidas['Jacarandá'])
    scatter_hd(lista_de_pares)
#%%
def grafico_altura_jacarandá():
    nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [(float(arbol['altura_tot']),arbol['diametro']) for arbol in arboleda if arbol['nombre_gen']=='Jacarandá']
    plt.hist(altos,bins=25)
#%%
def graficos_3_especies():
    nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    lista_de_pares=np.array(medidas['Eucalipto'])
    scatter_hd(lista_de_pares)
    lista_de_pares=np.array(medidas['Palo borracho rosado'])
    scatter_hd(lista_de_pares) 
    lista_de_pares=np.array(medidas['Jacarandá'])
    scatter_hd(lista_de_pares)
graficos_3_especies()