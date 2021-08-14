n = int(input("digite um inteiro: "))

x = 0
i = 1
j = 1

while x < n - 2:        
    i, j = j, i + j
    x+=1
    print(j)
