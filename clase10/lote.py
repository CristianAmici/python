import fileparse
class Lote:
    def __init__(self, nombre,cajones,precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones*self.precio
        
    def vender(self, cajones):
        self.cajones -= cajones
    def __str__(self):
        return f'Lote:{repr(self.nombre)}/{self.cajones}/${self.precio}'
    def __repr__(self):
        return f'Lote({self.nombre},{self.cajones},{self.precio})'
#%%
a =Lote('Pera', 100, 490.10)
b =Lote('Manzana', 50, 122.34)
c =Lote('Naranja', 75, 91.75)
lotes = [a, b, c]
print(a.vender())
#for c in lotes:
#     print(f'{c.nombre:>10s} {c.cajones:>10d} {c.precio:>10.2f}')
#%%
with open('../Data/camion.csv') as lineas:
    camion_dicts = fileparse.parse_csv(lineas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
#   print(camion)
#   print(sum([c.costo() for c in camion]))