# Validação do triangulo:
# Cada lado tem que ser > que diferença e < que a soma dos outros 2 lados.

a = float(input("lado a: "))
b = float(input("lado b: "))
c = float(input("lado c: "))

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
        print("Pode ser um triângulo!")
        if a == b == c:
                print("Triângulo Equilátero")
        elif a == b or b == c or c == a:
                print("Triângulo Isósceles")
        else:
                print("Triângulo Escaleno")
else:
        print("Não pode ser um triângulo!")       


