n = int(input("digite n: "))
k = 1
while k * (k+1) * (k+2) < n:
    k+=1
print(k * (k+1) * (k+2) == n)

n = int(input("digite n: "))
for i in range(n):
    if i * (i+1) * (i+2) == n:
        print(f"{i} * {i+1} * {i+2} = {n}")
        break
    
