#Definir ou obter a lista de números.
#Inicializar uma variável soma = 0.
#Percorrer a lista com for.
#Dentro do loop, usar if para testar se o número é par (num % 2 == 0).
#Se for par, adicionar à soma.
#Ao final, imprimir a soma.

lista = [1,2,3,4,5,6,7,8,9,10]
soma = 0

for list in lista:
    if list % 2 == 0:
        soma += list
        print("Soma dos números {}".format(soma))
    