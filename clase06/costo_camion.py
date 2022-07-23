import informe_funciones
def costo_camion(nombre_archivo):
    record=informe_funciones.leer_camion(nombre_archivo)
    suma=0
    for n_fila, fila in enumerate(record, start=1):
            try:
                ncajones = int(fila['cajones'])
                precio = float(fila['precio'])
                suma += ncajones * precio
            except:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return suma
#%%
def main():
   print(costo_camion('../Data/camion.csv'))
   
#main()
