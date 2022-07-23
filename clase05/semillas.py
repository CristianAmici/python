import random
random.seed(31415)

tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 

print(tirada)