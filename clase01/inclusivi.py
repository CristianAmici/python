frase = 'todos somos programadores'
palabras = frase.split()
frase_t=''
for palabra in palabras:
    
    if palabra[-2]=='o':
        frase_t = frase_t+' '+ palabra.split(-2)
    else:
        frase_t= frase_t+' '+palabra
print(frase_t)