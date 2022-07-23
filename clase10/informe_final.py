#!C:\Phyton python3
from lote import Lote 
import formato_tabla
from fileparse import parse_csv
from camion import Camion
#%%
def leer_camion(filename):
    '''
    Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.
    '''
    with open(filename) as file:
        camiondicts = parse_csv(file,
                                        select = ['nombre', 'cajones', 'precio'],
                                        types = [str, int, float])

    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
    
#%%
def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = parse_csv(f, types = [str, float], has_headers = False)
    return precios
#%%
def hacer_informe(lista_cajones,precios):
    lista=[]
    for compra in lista_cajones:
        cambio=precios[compra.nombre]-float(compra.precio)
        tupla=(compra.nombre,int(compra.cajones),float(compra.precio),cambio)
        lista.append(tupla)
    return lista
#%%
def imprimir_informe(data_informe, formateador):
    
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
#%%
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
     # Leer archivos con datos
   camion = leer_camion(nombre_archivo_camion)
   precios= leer_precios(nombre_archivo_precios)
   precios= {producto[0]:producto[1] for producto in precios}
    # Crear los datos para el informe
   informe = hacer_informe(camion, precios)
   # Imprimir el informe
   formateador = formato_tabla.crear_formateador(fmt)
   imprimir_informe(informe, formateador)
#%%
def f_principal(informe):
    informe_camion(informe[1],informe[2],informe[3])

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print("El programa necesita 3 o 4 argumentos.")
    else:
        # argumentos = sys.argv[1].split()
        f_principal(sys.argv)