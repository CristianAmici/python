import csv 
#%%
def parse_csv(nombre_archivo, types, has_headers= True, select = None, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    try:
          filas = csv.reader(nombre_archivo)

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
          for i, fila in enumerate(filas): 
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
            except Exception as e:
                if not silence_errors:
                    print("fila",i,":",fila)
                    print("fila",i,': motivo:',e)
          return registros
    except Exception as e:
          if not silence_errors:
              print("Para seleccionar, necesito encabezados.",e)
#camion=parse_csv('../Data/missing.csv', types = [str, int, float])
#print(camion)
