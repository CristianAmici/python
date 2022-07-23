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
                print('cuidado no hay tupla')
    return diccionario
def balance_del_negocio(archivo_camion,archivo_precios):
    camion = leer_camion(archivo_camion)
    diccionario= leer_precios(archivo_precios)
    balance=0;
    for compra in camion:
        costoCamion=float(compra['precio'])*int(compra['cajones'])
        ventaNegocio=diccionario[compra['nombre']]*float(compra['cajones'])
        balance+=ventaNegocio-costoCamion
    print('El balance del negocio es', round(balance,2))
