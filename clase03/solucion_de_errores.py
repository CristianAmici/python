#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era que ese codigo funciona si empieza con a, para que soporte el "contenga" necesita
# que solo haya una condicion SI tiene "a", sino tiene cuando sale del while devuelve falso. Ademas para que tome
#las A mayusculas es importante no olvidarse poner el metodo lower().
#    Lo corregí quitando el else y devolviendo false cuando sale del while, tambien agregando el metodo lower() para que
#soporte las A mayusculas.
#A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era que faltan los 2 puntos en la funcion, em eñ While y en el If, ademas para que tome
#las A mayusculas es importante no olvidarse poner el metodo lower().
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i].lower() == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era no considerar un int como string, ya que no tiene el metodo len().
#Lo corregi pasando la expresion que ingresa siempre a string, asi es mas facil y rapido reutilizar el codigo.

def tiene_uno(expresion):
    expresion= str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El programa da lo que deberia, porque el metodo suma, realiza una suma de dos numeros y no los devuele,
#por eso c no tiene valor y no es el mismo c que el definido en la suma.
#Solucion retornar c en la funcion.


def suma(a,b):
    c = a + b
    return c 

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: El programa es que se pisan los valores a donde apuntan y terminan copiando todos el ultimo valor.
#Solucion: limpiar el puntero cuando se agrega el registro al camion. Asi se hace un nuevo llamado cada vez.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)