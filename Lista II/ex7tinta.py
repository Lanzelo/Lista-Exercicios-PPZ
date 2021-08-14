'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas
de tinta a serem compradas e o preço total.

Obs. : somente são vendidos um número inteiro de latas.
'''

# area a ser pintada em m² = ???
# cobertura da tinta =  1.0 litro a cada 3m²
# 1 lata pinta 18 * 3m² = 54m²
# 1 lata de tinta = 18.0 litros por R$80.00

a = float(input("Área a ser pintada (em m²): "))
#latas = area / 54
#print(f"{latas} latas de tinta")

if a % 54 == 0:
    latas = int(a/54)
else:
    latas = int(a/54)+1

print(f"Qtd. Latas: {latas}")
print(f"Custo: R${latas*80:.2f}")
