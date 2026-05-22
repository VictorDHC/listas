pares = []
impares = []
for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
junta = pares + impares
print(f"pares:   {pares}")
print(f"impares: {impares}")
print(f"juntos:  {junta}")