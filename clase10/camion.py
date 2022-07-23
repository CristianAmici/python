class Camion:
    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def __contains__(self, nombre):
        return any(lote.nombre == nombre for lote in self.lotes)

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    def length(self):
        return len(self.lotes)
    def __getitem__(self,index):
        return self.lotes[index]
    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    def __repr__(self):
        print([lote.__repr__() for lote in self.lotes])
    def __srt__(self):
        print("Camion con "+Camion.length()+"lotes:" )
        for lote in self.lotes:
            print("Lote de"+lote.cajones+" cajones de "+ lote.nombre + ", pagados a "+lote.precio+" cada uno.")