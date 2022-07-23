# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        if type(data_fila)==dict:
            for colname in data_fila.keys():
                
                print(f'{data_fila[colname]:>10}', end=' ')
            print()
        else:
            for colname in data_fila.keys():
                print(f'{colname(data_fila, colname):>10s}', end=' ')
            print()
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
     '''
     Generar una tabla en formato HTML
     '''
     def encabezado(self, headers):
          print('<tr>', end=' ')
          for h in headers:
            print(f'<th>{h}</th>', end=' ')
          print('</tr>')

     def fila(self, data_fila):
           print('<tr>', end=' ')
           for d in data_fila:
            print(f'<td>{d}</td>', end=' ')
           print('</tr>')
def crear_formateador(nombre):
    if nombre=="html":
        return FormatoTablaHTML()
    elif nombre=="csv":
        return FormatoTablaCSV()
    elif nombre=="txt":
        return FormatoTablaTXT()
def imprimir_tabla(camion, headers, formateador):
     formateador.encabezado(headers)
     for lote in camion:
         formateador.fila(lote)