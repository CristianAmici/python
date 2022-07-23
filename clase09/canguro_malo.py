
class Canguro:
    def __init__(self,nombre,inicial=None):
        if inicial is None:
           self.contenido_marsupio  = []
            
        else:
           self.contenido_marsupio  = [inicial]
        self.nombre = nombre
        
    def meter_en_marsupio(self,elemento):
        self.contenido_marsupio.append(elemento)
    def __str__(self):
        ListaCanguro=["El canguro se llama " + self.nombre + ", En su bolsa tiene:  "]
        if len(self.contenido_marsupio)==0:
            print("El canguro se llama " + self.nombre + ", No tiene nada en su bolsa.")
        else: 
            for cosa in self.contenido_marsupio:
                ListaCanguro.append(cosa.__str__())
            print(ListaCanguro)
        
cangurito= Canguro("pepito")
madreCanguro= Canguro("Pepa",["perro","cocodrilo"])
print(cangurito.__str__())
#%%
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)