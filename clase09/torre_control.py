class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
#%%
class torre_control:
    def __init__(self):
        '''Crea una cola vacia.'''
        self.avionesPorDespegar = []
        self.avionesPorAterrisar = []

    def nuevo_arribo(self, avion):
        '''Encola el elemento x.'''
        self.avionesPorDespegar.append(avion)
    def asignar_pista(self):
        "asignar primero la pista para los que quieres aterrizar despues los despegar"
        if not self.esta_vacia(self.avionesPorAterrisar):
            vuelo=self.avionesPorAterrisar.pop(0)
            print("El vuelo "+ vuelo+" aterrizó con éxito.")
        elif not self.esta_vacia(self.avionesPorDespegar):
            vuelo=self.avionesPorDespegar.pop(0)
            print("El vuelo "+ vuelo+" despego con éxito.")
        else:
            print("No hay vuelos en espera.")
    def nueva_partida(self, avion):
        if self.esta_vacia(self.avionesPorDespegar):
            raise ValueError('La cola esta vacia')
        self.avionesPorAterrisar.append(self.items.pop(0))

    def esta_vacia(self,lista):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(lista) == 0
    def ver_estado(self):
        print("Vuelos esperando para aterrizar:", end="")
        print(avion +", " for avion in self.avionesPorAterrisar)
        print("Vuelos esperando para despegar:", end="")
        print(avion+"," for avion in self.avionesPorDespegar)
#%%
class Pila:
    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def apilar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desapilar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
#%%
def mostrar_x_del_estado(estado):
    print(f"Ejecutando {estado['función']}(), x vale {estado['variables']['x']}")
def f():
    x = 50
    a = 20
    print("En f, x vale", x)
def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)
pila_de_llamadas = Pila()
#la ejecución está en la línea 3 de g(). El estado tiene x=10.
estado = {'función': 'g', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 10, 'b': 45}}
mostrar_x_del_estado(estado)
#sigo ejecutando, toca llamar a f(): incremento y apilo el estado.
estado['próxima_línea_a_ejecutar'] = 5
pila_de_llamadas.apilar(estado)
#llamo a f y ejecuto primeras líneas
estado = {'función': 'f', 'próxima_línea_a_ejecutar': 3, 'variables': {'x': 50, 'a': 20}}
mostrar_x_del_estado(estado)
#termina ejecución de f: se desapila el estado:
estado = pila_de_llamadas.desapilar()
mostrar_x_del_estado(estado)