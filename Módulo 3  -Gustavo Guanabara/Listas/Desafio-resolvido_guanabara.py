#Faça um programa que leia 5 valores numericos e guarde-as em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista  

lista = []

for contador in range(0,5):
    lista.append(int(input("Digite um número: ")))