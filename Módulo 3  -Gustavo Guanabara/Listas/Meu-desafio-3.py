#crie um programa que vai ler vários números e colocar em uma lista depois disso mostre:
#Quantos números foram digitados
#A lista de valores ordenada forma decrescente
#Se o valor 5 foi digitado e está ou não na lista


lista = []

while True:
    valores = int(input("Digite um valor"))
    lista.append(valores)
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("ERRO!")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print(f"Você digitou {lista}")

lista.sort(reverse=True)
print(f"Lista com a ordem decrescente = {lista}")


if 5 in lista:
    print("O 5 está na lista")
else:
    print("O 5 não está na lista")
    




    
    
