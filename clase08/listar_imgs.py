import os
def archivos_png(directorios):
    listaFinal=[]
    directorio= os.listdir(directorios)
    for archivo in directorio:
        ext= archivo.split(".")
        if len(ext)>1:
            if ext[len(ext)-1]=='png':
                listaFinal.append(archivo)
    print(listaFinal)
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("El programa necesita 2 argumentos.")
    else:
        archivos_png(sys.argv[1])