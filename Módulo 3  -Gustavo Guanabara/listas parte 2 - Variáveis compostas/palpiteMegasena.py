from random import  randint


def PalpiteMegassena():
    lista = []
    jogos = []
    total = 1

    palpites = int(input("Quantas cartelas? "))

    while total <= palpites:
        contador = 0

        while True:
            numerosAposta = randint(1, 60)

            if numerosAposta not in lista:
                lista.append(numerosAposta)
                contador += 1

            if contador >= 6:
                break

        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        total += 1

    for posicao, tabela in enumerate(jogos):
        print(f"Jogo {posicao+1} = {tabela}")


#--------
PalpiteMegassena()
