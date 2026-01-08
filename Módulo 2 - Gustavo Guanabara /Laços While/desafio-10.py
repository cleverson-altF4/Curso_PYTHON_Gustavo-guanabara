resposta = 'S'
soma = 0
media = 0
quantidade = 0
maior = menor = 0

while resposta == 'S':
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1

    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    while True:
        resposta = input("Quer continuar? [S/N]: ").strip().upper()
        if resposta and resposta[0] in 'SN':
            resposta = resposta[0]
            break
        print("Erro! Digite apenas S ou N.")

if quantidade > 0:
    media = soma / quantidade
    print("\nA média dos números digitados é =", media)
    print("A quantidade de números foi =", quantidade)
    print("Maior =", maior, "Menor =", menor)
else:
    print("Nenhum número foi digitado.")
