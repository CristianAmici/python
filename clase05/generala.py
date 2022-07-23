import random
#%%
def tirar():
   tirada=[]
   listaFinal=[];
   guardado=[];
   for i in range(5):
       tirada.append(random.randint(1,6))
   dado1=tirada.count(tirada[0])
   dado2=tirada.count(tirada[1])
   dado3=tirada.count(tirada[2])
   dado4=tirada.count(tirada[3])
   if dado1>=dado2 and dado1>=dado3 and dado1>=dado4:
       guardado=tirada[0]
       rango=dado1
   elif dado2>dado1 and dado2>=dado3 and dado2>=dado4:
       guardado=tirada[1]
       rango=dado2
   elif dado3>dado1 and dado3>dado2 and dado3>=dado4:
       guardado=tirada[2]
       rango=dado3
   else:
       guardado=tirada[3]
       rango=1;
   for k in range(rango):
       tirada.remove(guardado)
       listaFinal.append(guardado)
   rangoTirada=len(tirada)
   tirada.clear()
   if rangoTirada>0:
       for i in range(rangoTirada):
           tirada.append(random.randint(1,6))
   for i in range(rangoTirada):
       if tirada[i]==guardado:
           listaFinal.append(tirada[i])
   rangoTirada= 5-len(listaFinal)
   tirada.clear()
   if rangoTirada>0:
       for i in range(rangoTirada):
           tirada.append(random.randint(1,6))
   listaFinal+=tirada
   return listaFinal
#%%
def es_generala(tirada):
    return tirada[0]==tirada[1]==tirada[2]==tirada[3]==tirada[4]
    

#%%
def prob_generala(N):
    
    G = sum([es_generala(tirar()) for i in range(N)])
    print(f'Tiré {N} veces, de las cuales {G} saqué generala.')
    prob = G/N
    return prob
#%%
#N=1000000
#prob=prob_generala(N)

#print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')