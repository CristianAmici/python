def diccionario_geringoso(listaDePalabras):
   diccionario={}
   for cadena in listaDePalabras:
       cadenaFinal=''
       for c in cadena:
           cadenaFinal+=c
           if c=='a':
               cadenaFinal+= 'pa'
           elif c=='e':
               cadenaFinal+= 'pe'
           elif c=='i':
               cadenaFinal+= 'pi'
           elif c=='o':
               cadenaFinal+= 'po'
           elif c=='u':
               cadenaFinal+= 'pu'
               
       diccionario[cadena]=cadenaFinal
   return diccionario           

lista=['banana', 'manzana', 'mandarina']
print(diccionario_geringoso(lista))
