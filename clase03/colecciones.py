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

camion = leer_camion('../Data/camion.csv')
from collections import Counter
tenencias = Counter()
for s in camion:
        tenencias[s['nombre']] += int(s['cajones'])

print(tenencias)
camion2 = leer_camion('../Data/camion2.csv')
from collections import Counter
tenencias2 = Counter()
for s in camion2:
        tenencias2[s['nombre']] += int(s['cajones'])

print(tenencias2)
combinada=tenencias + tenencias2
print(combinada)
