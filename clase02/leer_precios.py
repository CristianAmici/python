def leer_precios(nombre_archivo):
    import csv
    
    diccionario={}
    with open(nombre_archivo, 'r') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                diccionario[row[0]]= row[1]
            except:
                print('cuidado no hay tupla')
    return diccionario

precios = leer_precios('../Data/precios.csv')
print(precios['Naranja'])