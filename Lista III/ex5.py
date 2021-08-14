a = int(input("digite o 1º numero: "))
b = int(input("digite o 2º numero: "))

while a % b != 0:
    a, b = b, a % b
print(b)
