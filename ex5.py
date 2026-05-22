ls = ["pera", "uva", "abacaxi", "banana", "morango"]
maior = ls[0]
menor = ls[0]
for p in ls:
    if len(p) > len(maior):
        maior = p
    if len(p) < len(menor):
        menor = p
print(f"Maior palavra: {maior}")
print(f"Menor palavra: {menor}")
