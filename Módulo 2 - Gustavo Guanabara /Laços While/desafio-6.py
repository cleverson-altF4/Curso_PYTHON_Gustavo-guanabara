#escreva um programa que leia um número N qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci

#F(0) = 0
#F(1) = 1
# F(n) = F(n−1) + F(n−2)

#a, b = b, a + b   

a = 0
b = 1
contador = 0
n = int(input("Fibonacci: "))

while contador < n:
    print(a, end= ' ')
    a, b = b, a + b
    contador += 1
