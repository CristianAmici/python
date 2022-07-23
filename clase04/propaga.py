def propagar(lista):
    for index, f in enumerate(lista):
        if f ==1:
            pos=index+1
            while pos<=len(lista)-1 and lista[pos]==0:
                lista[pos]=1
                pos=pos+1
            pos=index-1
            while  pos>=0 and lista[pos]==0:
                lista[pos]=1
                pos=pos-1
    return lista
print(propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
print(propagar([ 0, 0, 0, 1, 0, 0]))