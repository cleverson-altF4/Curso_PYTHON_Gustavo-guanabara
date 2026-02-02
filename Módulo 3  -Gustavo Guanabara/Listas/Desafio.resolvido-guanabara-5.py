#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares digitados respectivamente. Ao final mostre o conteúdo das 3 listas geradas

numero = []
par = []
impar = []

while True:
    numero.append(int(input("Digite um número: ")))
    resposta = str(input("Deseja continuar? [S/N]: "))
    if resposta in 'Nn':
        break
    
for i, valor in enumerate(numero):
    if valor % 2 == 0:
        par.append(valor)
    elif valor % 2 == 1:
        impar.append(valor)
    

        
print("*"*30)
print(f"Números digitados {numero}")
print(f"Números pares {par}")
print(f"Números ímpares {impar}")