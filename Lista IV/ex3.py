import random

k1 = random.sample(range(101), 10)
k2 = random.sample(range(101), 10)
k3 = []

for i in range(10): #range 10 pq a cada for ele adiciona 2 (k1 e k2). 2*10=20
    k3.append(k1[i])
    k3.append(k2[i])

# for i in zip(k1, k2): zip junta os elementos de 2 listas numa só
#    k3.extend(list(i))

print(f"k1: {k1}\nk2: {k2}\nk3: {k3}")
