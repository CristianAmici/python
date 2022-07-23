from fileparse import parse_csv
#%%
def leer_camion(nombre_archivo):
    return parse_csv(nombre_archivo, types=[str,int,float], has_headers=True)
   
#%%
def leer_precios(nombre_archivo):
    return parse_csv(nombre_archivo, types=[str,float], has_headers=False)
#%%
def hacer_informe(lista_cajones,precios):
    lista=[]
    for compra in lista_cajones:
        cambio=precios[compra['nombre']]-float(compra['precio'])
        tupla=(compra['nombre'],int(compra['cajones']),float(compra['precio']),cambio)
        lista.append(tupla)
    return lista
#%%
def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'%headers)
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        print(f'{nombre:>10s} {cajones:>10d}    ${precio:6.2f} {cambio:>10.2f}')
#%%
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios= leer_precios(nombre_archivo_precios)
    precios= {producto[0]:producto[1] for producto in precios}
    informe= hacer_informe(camion,precios);
    imprimir_informe(informe)
    
#informe_camion('../Data/camion.csv', '../Data/precios.csv')
#informe_camion('../Data/camion2.csv', '../Data/precios.csv')