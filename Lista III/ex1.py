
while True:  
    n = int(input("digite uma nota de 0 a 10: "))
    if n < 0 or n > 10:
        print("valor invalido")
        continue # retornar ao inicio do codigo
    else:
        print("valor aceito")
        break # finalizar o codigo
'''
n = int(input("digite uma nota de 0 a 10: "))
while n < 0 or n > 10:
    print("valor invalido")
    n = int(input("digite uma nota de 0 a 10: "))
print("valor aceito")
'''
