import math
resposta = 'S'
media = 0
soma = 0
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
        print("\nDeseja continuar?\n")
        resposta = str(input("S/N: ")).strip().upper()
        if resposta and resposta[0] in 'SN':
            resposta = resposta[0]
            break
        print("Erro ao continuar. Digite apenas [S/N]")
        
if quantidade > 0:
    media = soma / quantidade
    media = math.floor(media)
    print("Media = {}".format(media))
    print("Quantidade de números digitados = {}".format(quantidade))
    print("Maior número: {}".format(maior))
    print("Menor número = {}".format(menor))
else:
    print("Não há números.")