import random

par, impar = [], []
lista = random.sample(range(101), 20)
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])
print(f"lista: {lista}\npar: {par}\nimpar: {impar}")
'''
#list comprehension: pode gerar a lista dentro dos colchetes
lista = random.sample(range(101), 20)
par = [i for i in lista if i % 2 == 0]
impar = [i for i in lista if i % 2 == 1]
print(f"lista: {lista}\npar: {par}\nimpar: {impar}")
'''
