def leer_camion(nombre_archivo):
    import csv
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)
        for fila in filas:
            record = dict(zip(headers, fila))
            camion.append(record)
    return camion

def leer_precios(nombre_archivo):
    import csv
    
    diccionario={}
    with open(nombre_archivo, 'r') as f:
        filas = csv.reader(f)
       #headers=['nombre', 'cajones', 'precio']
        for fila in filas:
            try:
                diccionario[fila[0]]= float(fila[1])
            except:
                print('...')
    return diccionario

def hacer_informe(lsita_cajones,precios):
    lista=[]
    for compra in camion:
        cambio=precios[compra['nombre']]-float(compra['precio'])
        tupla=(compra['nombre'],int(compra['cajones']),float(compra['precio']),cambio)
        lista.append(tupla)
    return lista

camion = leer_camion('../Data/fecha_camion.csv')
diccionario= leer_precios('../Data/precios.csv')
informe= hacer_informe(camion,diccionario);
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
print('%10s %10s %10s %10s'%headers)
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')


    
