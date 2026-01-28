#Crie um programa que onde o usuário possa digitar 5 valores númericos e cadastre-os em uma lista.
#Já na posição correta de inserção(sem usar Sort())
#NO final mostre a lista ordenada na tela
lista = []

for i in list(range(1,6)):
    usuario = int(input("Digite um valor: "))
    
    if len(lista) == 0:
        lista.append(usuario)
   
