import random
def prov_envido(veces):
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(valor,palo) for valor in valores for palo in palos]
    contador=0
    
    for i in range(veces):
        envido=20
        cartas=random.sample(naipes,k=3)
        if cartas[0][0]==10 or cartas[0][0] ==11 or cartas[0][0]==12:
            cartas[0][0]==0
        if cartas[1][0]==10 or cartas[1][0] ==11 or cartas[1][0]==12:
            cartas[1][0]==0
        if cartas[2][0]==10 or cartas[2][0] ==11 or cartas[2][0]==12:
            cartas[2][0]==0
        if cartas[0][1]==cartas[1][1]:
            envido+= cartas[0][0]+cartas[1][0]
        elif  cartas[0][1]==cartas[2][1]:
             envido+= cartas[0][0]+cartas[2][0]
        elif cartas[1][1]==cartas[2][1]:
            envido+= cartas[1][0]+cartas[2][0]
        
        if envido==33:
            contador+=1 
    return contador

print(prov_envido(1000000)/1000000)