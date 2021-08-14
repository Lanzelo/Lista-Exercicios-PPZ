u = input("digite um nome usuario: ")
while True:
    s = input("digite uma senha: ")
    if u == s:
        print("erro 42: senha não pode ser igual a nome de usuário! por favor, digite outra senha.")
    else:
        print("usuario cadastrado com sucesso!")
        break
