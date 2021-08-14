import random

lista = random.sample(range(101), 10)
print(lista) # não pode imprimir a lista da amostra direto
maior = menor = lista[0]
for i in range(10): #até i percorrer a lista toda
    if lista[i] > maior: maior = lista[i] #se o prox num for maior, = maior
    if lista[i] < menor: menor = lista[i] #se o prox num for menor, = menor

print(f"o maior número é {maior} e o menor número é {menor}")
