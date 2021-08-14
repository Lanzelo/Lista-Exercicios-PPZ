a = 80000
b = 200000
t = 0

while a < b:
    a = a + (a * 0.030)
    b = b + (b * 0.015)
    t+=1
print(f"Em {t} anos, o país A terá uma população maior que o país B")
# Resposta: 63 anos
