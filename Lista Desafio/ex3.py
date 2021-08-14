'''
n = int(input("numero: "))
k=1
div=0
while k <= n:
    if n%k == 0:
        div = div + 1
    k+=1
print(div == 2) # se é V ou F


i, div = 1, 0
for i in range(n):
    if n % (i+1) == 0:
        div+=1
print(div == 2)
'''

n = 2
k = 0
while n <= 100: 
    if n == 2 or n ==3 or n ==5 or n ==7 or (n%2 != 0 and n%3 != 0 and n%5 != 0 and n%7 != 0):
        print(str(n))
        k+=1
    n+=1
    if k == 10:
        break
