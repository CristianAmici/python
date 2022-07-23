import numpy as np
import matplotlib.pyplot as plt

def ajuste_lineal_simple(x,y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b
superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])
g = plt.scatter(x = superficie, y = alquiler)
plt.title('scatterplot de los datos')
plt.show()

N = 50
minx = 0
maxx = 500
superficie = np.random.uniform(minx, maxx, N)
r = np.random.normal(0, 25, N) # residuos simulados
alquiler = 1.3*superficie + r
g = plt.scatter(x = superficie, y = alquiler)
plt.title('gráfico de dispersión de los datos')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

a, b = ajuste_lineal_simple(superficie,alquiler)

grilla_x = np.linspace(start = minx, stop = maxx, num = 1000)
grilla_y = grilla_x*a + b

g = plt.scatter(x = superficie, y = alquiler)
plt.title('y ajuste lineal')
plt.plot(grilla_x, grilla_y, c = 'green')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())