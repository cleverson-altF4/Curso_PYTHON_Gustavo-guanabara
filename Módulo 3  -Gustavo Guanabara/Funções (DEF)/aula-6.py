#faça um programa que tenha uma função chamada contador() que receba 3 parâmetros, INICIO, FIM, PASSO e realize uma contagem 

#Seu programa tem que realizar 3 contagens através da função criada

#A) de 1 até 10, de 1 em 1
#B0 de 10 até 0, de 2 em 2
#Uma contagem personalizado 
from time import sleep

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))


def contador(inicio, fim, passo):
    for i in range(inicio, fim, passo):
        print(f"{i}",end=' ')
        sleep(0.5)
        
        
        
        
contador(inicio, fim, passo)