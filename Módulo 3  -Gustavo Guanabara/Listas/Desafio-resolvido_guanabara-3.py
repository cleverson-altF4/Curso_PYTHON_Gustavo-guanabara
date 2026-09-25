"""Lista ordenada dinâmica"""

listaVazia = []

for indice in range(0, 5):
    numero = int(input("Digite um número: "))

    if indice == 0 or numero > listaVazia[len(listaVazia)-1]:
        listaVazia.append(numero)
        print("adicionado no final da lista")
    else:
        posicaoCorreta = 0

        while posicaoCorreta < len(listaVazia):
            if numero <= listaVazia[posicaoCorreta]:
                listaVazia.insert(posicaoCorreta
                                 ,numero)
                print(f"Inserido na posição {posicaoCorreta}")
                break
            posicaoCorreta += 1


resultado = listaVazia
print(resultado)

