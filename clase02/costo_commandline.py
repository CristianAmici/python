def costo_camion(nombre_archivo):
    import sys
    import csv
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = '../Data/camion.csv'
    suma=0
    f = open(nombre_archivo, 'rt')
    rows= csv.reader(f)
    next(rows)
    for line in rows:
        try:
            suma+=int(line[1])*float(line[2])
        except:
            print('warning')
    return suma


costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)
