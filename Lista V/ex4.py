k = 0
for i in range(18644, 33087):
    if '2' in str(i) and '7' not in str(i): # int não é iterável em python, converter para texto
        k+=1
print(k)
