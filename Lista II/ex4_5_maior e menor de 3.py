a = int(input("digite o 1º número: "))
b = int(input("digite o 2º número: "))
c = int(input("digite o 3º número: "))

print(f"numeros {a}, {b}, {c}")
if a > b and a > c:
    print(f"Maior número: {a}")
elif b > c:
    print(f"Maior número: {b}")
else:
    print(f"Maior número: {c}")

if a < b and a < c:
    print(f"menor número: {a}")
elif b < c:
    print(f"menor número: {b}")
else:
    print(f"menor número: {c}")

