#Definir a lista de números.
#Inicializar maior_impar = None.
#Percorrer a lista com for.
#Para cada número, verificar if num % 2 != 0.
#Se for ímpar e (maior_impar é None ou num > maior_impar), atualizar maior_impar.
#Após o loop, checar se maior_impar ainda é None e imprimir resultado.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
maior_impar = None

for list in lista:
    if list % 2 != 0:
        if maior_impar is None or list > maior_impar:
            maior_impar = list

if maior_impar is None:
    print("Não há números ìmpares")
else:
    print("Maior ìmpar", maior_impar)