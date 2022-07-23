import informe_final
def costo_camion(nombre_archivo):
    record=informe_final.leer_camion(nombre_archivo)
    suma=0
    for n_fila, fila in enumerate(record, start=1):
            try:
                ncajones = int(fila.cajones)
                precio = float(fila.precio)
                suma += ncajones * precio
            except:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return suma

#%%
def f_principal(informe):
    print(costo_camion(informe[1]))
#%%
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("El programa necesita dos argumentos.")
    else:
        # argumentos = sys.argv[1].split()
        f_principal(sys.argv)