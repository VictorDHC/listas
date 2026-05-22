ls = []
frase = input("Insira: ")
palavra = ""
for letra in frase:
    if letra != " ":
        palavra += letra
    else:
        ls.append(palavra)
        palavra = ""
ls.append(palavra)
print(ls)