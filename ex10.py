tab = [" "] * 9
jogador = "X"
for turno in range(9):
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    pos = int(input(f"vez do {jogador}. Escolha a posição (0-8): "))
    if tab[pos] != " ":
        print("posição ocupada!")
        break
    tab[pos] = jogador
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    ganhou = False
    for c in combos:
        if tab[c[0]] == tab[c[1]] == tab[c[2]] == jogador:
            ganhou = True
    if ganhou:
        print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
        print("---+---+---")
        print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
        print("---+---+---")
        print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
        print(f"{jogador} venceu!")
        break
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"
else:
    print(f" {tab[0]} | {tab[1]} | {tab[2]} ")
    print("---+---+---")
    print(f" {tab[3]} | {tab[4]} | {tab[5]} ")
    print("---+---+---")
    print(f" {tab[6]} | {tab[7]} | {tab[8]} ")
    print("Empate!")