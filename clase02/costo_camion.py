def costo_camion(nombre_archivo):
    import csv
    f = open(nombre_archivo, 'rt')
    filas= csv.reader(f)
    encabezados=next(filas)
    suma=0
    for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            try:
                ncajones = int(record['cajones'])
                precio = float(record['precio'])
                suma += ncajones * precio
            except:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return suma


costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
costo= costo_camion('../Data/fecha_camion.csv')
print('Costo total:', costo)