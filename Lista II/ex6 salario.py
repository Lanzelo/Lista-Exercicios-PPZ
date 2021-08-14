'''
a. + Salário Bruto : R$
b. - IR (11%) : R$
c. - INSS (8%) : R$
d. - Sindicato ( 5%) : R$
e. = Salário Liquido : R$
'''

bruto = float(input("Bruto R$: "))

ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05

deducoes = ir + inss + sind

liq = bruto - deducoes

print(f"IR: R${ir:.2f}")
print(f"INSS: R${inss:.2f}")
print(f"Sindicato: R${sind:.2f}")
print(f"Salário Liquido: R${liq:.2f}")

