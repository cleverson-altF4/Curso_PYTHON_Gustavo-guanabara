#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso crie duas listas extras que vão conter apenas valores pares e os ímpares digitados respectivamente.
#Ao final mostre o conteúdo contendo das 3 listas geradas
lista = []
lista_par = []
lista_impar = []

while True:
    numero = int(input("Digite um número: "))
    lista.append(numero)
    
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim ou Nao]: ")).strip().upper()
        if continuar == '':
            print("ERRO!")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("*"*40)
print()
print("Todos os números da lista = {}".format(lista))
print(f"Todos os pares = {lista_par}")
print(f"Todos os números ímpares = {lista_impar}")