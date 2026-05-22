import random
lis = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(lis)
letra = input("Qual letra você quer adivinhar a posição? ")
chute = int(input(f"em qual posição (0-25) está o '{letra}'? "))
pos_real = lis.index(letra)
if chute == pos_real:
    print("acertou!")
else:
    print(f"errou! A posição correta era {pos_real}")