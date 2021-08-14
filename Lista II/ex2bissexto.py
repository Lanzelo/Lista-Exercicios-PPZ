ano = int(input("ano: "))

#condições ano bissexto: 
#1) multiplo de 400
if ano % 400 == 0:
        print(f"{ano} é ano Bissexto")

#2) multiplo de 4, mas não multiplo de 100
elif ano % 4 == 0 and ano % 100 != 0:
        print(f"{ano} ano Bissexto")
        
else:
        print(f"{ano} não é Ano Bissexto")
