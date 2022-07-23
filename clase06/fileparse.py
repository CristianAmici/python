import csv 
#%%
def parse_csv(nombre_archivo, types, has_headers= True, select = None):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)

        # Lee los encabezados del archivo
        if has_headers:
            encabezados = next(filas)
        indices=[]
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
        if has_headers:
           if select:
               indices = [encabezados.index(nombre_columna) for nombre_columna in select]
               encabezados = select
           else:
               indices = []

        registros = []
        for fila in filas:
            try:
                if not fila:    # Saltear filas vacías
                   continue
                if types:
                   fila = [func(val) for func, val in zip(types, fila) ]
                   # Filtrar la fila si se especificaron columnas
                if indices:
                   fila = [fila[index] for index in indices]

                if has_headers:
                   registro = dict(zip(encabezados, fila))
                else:
                   registro=fila;
                registros.append(registro)
            except:
                print(f' No pude interpretar: {fila}')
    return registros
#print(parse_csv('../Data/precios.csv', types=[str,float], has_headers=False))