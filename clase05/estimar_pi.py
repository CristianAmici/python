import random
def generar_punto():
    x = round(random.random(),2)
    y = round(random.random(),2)
    return x,y


def estimar_pi(n):
    lista=[]
    tupla=()
    for i in range(n):
        tupla= generar_punto()
        if (tupla[0]**2 +tupla[1]**2) < 1:
            lista.append(tupla)
    return len(lista)/n
print(estimar_pi(100000))