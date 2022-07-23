from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]
        
def filtrar_datos(rows, nombres):
    filas = (row for row in rows if row['nombre'] in nombres)
    for fila in filas:
        yield row

def ticker(camion_file, log_file, fmt):
    formateador= crear_formateador(fmt)
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    for i, row in enumerate(rows):
        if i==0:
            formateador.encabezado(row.keys())
            formateador.fila(row)
        else:
            formateador.fila(row)
    
    
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)