import informe_final
def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.precio_total()

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