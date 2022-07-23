def buscar_precio(fruta):
    resultado=0
    f = open('../Data/precios.csv', 'rt')
    next(f)
    for line in f:
        row = line.split(',')
        if row[0]==fruta:
            resultado=float(row[1])
    f.close()
    if resultado!=0:
        print('El precio de un cajón de ',fruta,' es: ' , resultado)
    else:
        print(fruta,' no figura en el listado de precios.')
buscar_precio('Frambuesa')
buscar_precio('Kale')