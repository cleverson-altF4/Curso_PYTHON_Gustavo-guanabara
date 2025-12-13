#Leia um inteiro N do usuário.
#Inicialize soma = 0.
#Percorra i de 1 a N com for.
#Se i for par (i % 2 == 0), adicione à soma.
#Ao final, imprima a soma.

numero = int(input("Número N: "))
soma = 0
for i in range(1, numero+1):
    if i % 2 == 0:
        soma += i

print("A soma dos pares até",numero, "=", soma)