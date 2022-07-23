def tablaMult():
    lista=[]
    listaFinal={}
    for i in range(10):
        lista=[]
        valor=0
        for n in range(10):
            lista.append(valor)
            valor+=i
        tupla=()
        tupla=tuple(lista)
        listaFinal[i]=tupla
    header=listaFinal[1]
    print('%11d %6d %5d %5d %5d %5d %5d %6d %5d %5d'%header)
    print('--------------------------------------------------------------------')
    for i in listaFinal:
        tupla=listaFinal[i]
        print(f'{i:>5d}:{tupla[0]:>6d}{tupla[1]:>6d}{tupla[2]:>6d}{tupla[3]:>6d}{tupla[4]:>6d}{tupla[5]:>6d}{tupla[6]:>6d} {tupla[7]:>6d}{tupla[8]:>6d}{tupla[9]:>6d}')
tablaMult()  

