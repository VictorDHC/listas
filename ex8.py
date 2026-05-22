lis = []
for i in range(1, 11):
    lis.append(i ** 2)
soma = 0
for v in lis:
    soma += v
print(f"lista: {lis}")
print(f"soma: {soma}")