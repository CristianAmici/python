import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
colors=['blue','green','yellow','red','black','pink','orange','brown','purple','violet','grey','salmon']
valorMaximo=0
valorMinimo=100000000;
minList=[]
maxList=[]
fig = plt.figure(figsize=(8, 6), dpi=80)
plt.subplot(2, 1, 1)
plt.title("12 caminatas al azar")
plt.ylabel("Distancia desde el origen")
plt.xlabel("tiempo")
for i in range(12):
    tempList=randomwalk(N)
    plt.plot(tempList, color=colors[i])
    
    if(max(tempList, key=abs)>valorMaximo):
       maxList=tempList
       valorMaximo=max(tempList)
    elif(min(tempList)<valorMinimo):
        minList=tempList
        valorMinimo=min(tempList)

plt.subplot(2, 2, 3)
plt.title("El que mas se desvia +")
plt.ylabel("Distancia desde el origen")
plt.plot(maxList, color='red')
plt.xlabel("tiempo")
plt.subplot(2, 2, 4)
plt.title("El que mas se desvia -")
plt.plot(minList, color='blue')
plt.xlabel("tiempo")


plt.show()
n = 5
lista =["uno","dos","tres"]
print(lista[1])
d={}
print(len(d))

        