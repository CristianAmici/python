
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
        ListaCanguro=[]
        if len(self.contenido_marsupio)==0:
            return "El canguro se llama " + self.nombre + ", No tiene nada en su bolsa."
        else: 
            for cosa in self.contenido_marsupio:
                ListaCanguro.append(cosa.__str__())
            return "El canguro se llama"+ self.nombre+" y contiene"+ListaCanguro.__str__()
    def __repr__(self):
        return str(self.nombre)
        

#%%
# canguro_malo.py
"""Este código continene un 
bug importante y dificil de ver
"""

class Canguro_malo:
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
            #el error estaba en que si se llama al string de un objeto que no tiene definido su descripcion
            #se imprime el espacio en memoria del objeto, por eso tuve que redifinir otra funcion que sea general
            #para todos los objetos "repr()"
            s = '    ' + repr(obj)
            t.append(s)
        return '\n'.join(t)
    #hay que agregar una funcion de string individual para que no resulte recursivo el llamado al __str__
    #por eso esta bueno agregar la funcion __repr__() para poder llamar a todos los objetos y al mismo timepo
    #definirla en el objeto canguro
    def __repr__(self):
        return str(self.nombre)
    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)