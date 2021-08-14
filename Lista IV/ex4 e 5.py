texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'''

texto = texto.lower()
texto = texto.replace('.', '')
texto = texto.replace('.', '')
texto = texto.replace(':', '')
lista = texto.split(" ")

python = []
mais4 = []
for i in range(len(lista)):
    palavra = lista[i]
    if palavra[0] in 'python' or palavra[0] in 'python':
    #palavra[0] == "p" or palavra[0] == "y" or palavra[0] == "t" or palavra[0] == "h" or palavra[0] == "o" or palavra[0] == "n":
        python.append(lista[i])
    #elif palavra[len(palavra)-1] == "p" or palavra[len(palavra)-1] == "y" or palavra[len(palavra)-1] == "t" or palavra[len(palavra)-1] == "h" or palavra[len(palavra)-1] == "o" or palavra[len(palavra)-1] == "n":
    #    python.append(lista[i])
print(f"inicio/fim python: {python}")

for i in range(len(lista)):
    palavra = lista[i]
    k = 0
    if palavra[k] in 'python' and len(palavra) > 4:
        mais4.append(lista[i])
    k+=1
print(f"com letras python & +4: {mais4}")
