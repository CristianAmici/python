# vigilante.py
import os
import time

def vigilar(archivo):
    f = open(archivo)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.5)   # Esperar un rato y
            continue          # vuelve al comienzo del while
        fields = line.split(',')
        volumen = int(fields[2])
        if volumen > 1000:
            yield line

if __name__ == '__main__':
    import informe_final

    camion = informe_final.leer_camion ('../Data/camion.csv')

    for line in vigilar('../Data/mercadolog.csv'):
        fields = line.split(',')
        nombre = fields[0].strip('"')
        if nombre in camion:
            print(line)