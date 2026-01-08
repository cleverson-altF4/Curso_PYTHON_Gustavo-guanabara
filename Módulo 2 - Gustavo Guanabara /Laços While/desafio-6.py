#escreva um programa que leia um número N qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci

#F(a) = 0
#F(1) = 1
# F(n) = F(n−1) + F(n−2)

#a, b = b, a + b   

a, b = 0, 1
contador = 0
numero = int(input("Sequência de Fibonacci: "))

while contador < numero:
    print(a, end= ' - ')
    a,b = b, a + b
    contador += 1
