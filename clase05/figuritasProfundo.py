import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    album = np.zeros(figus_total,dtype=np.int64)
    return album

def album_incompleto(album):
    estado = 0 in album
    return estado

def comprar_figu(figus_total):
    figurita = random.choice([i for i in range(figus_total)])
    return figurita

def comprar_paquete(figus_total,figus_paquete):
    paquete = random.choices([i for i in range(figus_total)],k=figus_paquete)
    return paquete

def cuantas_figus(figus_total):
    album = crear_album(figus_total)   # Creamos el album vacio
    estado = True                     
    figuritas = 0
    while (estado == True):           # Mientras el album esté incompleto hacer...
        figuritas += 1
        figurita = comprar_figu(figus_total)   # Se compra una figurita
        album[figurita] += 1
        estado = album_incompleto(album)        
    return figuritas

def cuantos_paquetes(figus_total,figus_paquete):
    album = crear_album(figus_total)
    estado = True
    paquetes = 0
    while (estado == True):
        paquetes += 1
        paquete = comprar_paquete(figus_total,figus_paquete)
        for i in paquete:
            album[i] += 1
        estado = album_incompleto(album)
    return paquete

def experimento_figus(figus_total,n_repeticiones):
    lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    promedio = np.mean(lista)
    return promedio

def experimento_paquetes(figus_total,figus_paquete,n_repeticiones):
    lista = [cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)]
    promedio = np.mean(lista)
    return promedio

def calcular_historia_figus_pegadas(figus_total,figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas
        
        
def main():
    print('Consideremos primero el caso de comprar las figuritas por unidad.',end='\n\n')
    N = int(input('Ingresar el número total de figuritas en el álbum: '))
    S = int(input('Ingresar el número de simulaciones que quiere realizar: '))
    print('')
    print(f'En promedio hay que comprar {experimento_figus(N,S)} figuritas para completar el álbum.')
    print('\n')
    print('Consideramos ahora el caso de comprar las figuritas por paquete.',end='\n\n')
    N = int(input('Ingresar el número total de figuritas en el álbum: '))
    P = int(input('Ingresar el número de figuritas que vienen en un paquete: '))
    S = int(input('Ingresar el número de simulaciones que quiere realizar: '))
    print('')
    print(f'En promedio hay que comprar {experimento_paquetes(N,P,S)} paquetes para completar el álbum.')
    print('\n')
    print('Graficamos el llenado del album para una simulación:',end='\n\n')
    plt.plot(calcular_historia_figus_pegadas(N,P))
    plt.xlabel("Cantidad de paquetes comprados")
    plt.ylabel("Cantidad de figuritas pegadas")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
main()







def main():
    crear_album(670)
    album_incompleto(crear_album(670)) #True
    comprar_figu(670) #35
    cuantas_figus(670) #4387
    repetir_cuantas_figus(1000) #14.361
    experimento_figus(100, 670) #4624.52
    comprar_paquete(670, 5) #[91, 383, 144, 507, 446]
    cuantos_paquetes(670, 5) #1009
    experimento_paquetes(100) #954.2