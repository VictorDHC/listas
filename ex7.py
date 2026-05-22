lis = []
for i in range(1, 101):
    lis.append(i)
print("Pares: ", end="")
for v in lis:
    if v % 2 == 0:
        print(v, end=" ")