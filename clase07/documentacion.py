#%%
#precondicion= recibir un numero
def valor_absoluto(n):
    if n >= 0:
        return n
    else:
        return -n

#%%
#precondicion= recibir un lista iterable de numeros
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
#%%
#precondicion: recibir dos numeros enteros
def veces(a, b):
    #suma el parametro a tantas veces como b
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
#poscondicion: devuelve la suma del primero tantas veces como
#el segundo parametro
#invariante de ciclo: el parametro b debe ser distinto de 0
#%%
#precondicion= recibir un numero entero
def collatz(n):
    #cuanta la cantidad de veces que puede dividirse por 2 el numero ingresado
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
#poscondicion: devuelve la cantidad de veces que el numero 
#puede dividirse por 2
#invariante de ciclo: el parametro n debe ser distinto de 1