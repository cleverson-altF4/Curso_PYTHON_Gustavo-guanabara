#crie um programa que vai ler vários números e colocar em uma lista depois disso mostre:
#Quantos números foram digitados
#A lista de valores ordenada forma decrescente
#Se o valor 5 foi digitado e está ou não na lista
valores = []

while True:
    valores.append(int(input("Digite um valor: ")))
    resposta = str(input("Deseja continuar? [Sim/Não: "))
    if resposta in 'Nn':
        break
    
print("*"*30)
print("Números digitados {}".format(valores))
valores.sort(reverse= True)
print(f"Números em ordem decrescente {valores}")

if 5 in valores:
    print("O 5 está na lista")
else:
    print("O 5 não está na lista")