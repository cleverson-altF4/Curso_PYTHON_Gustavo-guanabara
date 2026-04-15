#faça um programa que tenha uma função chamada contador() que receba 3 parâmetros, INICIO, FIM, PASSO e realize uma contagem 

#Seu programa tem que realizar 3 contagens através da função criada

#A) de 1 até 10, de 1 em 1
#B0 de 10 até 0, de 2 em 2
#Uma contagem personalizado 
from time import sleep

def linha():
    print("-"*55)
    
    
def contar(inicio, fim, passo):
    contar_numero = inicio
    
    if inicio < fim:
        
        if passo < 0:
            passo *= -1
            
        if passo == 0:
            passo += 1
        
        while contar_numero < fim:
            print(contar_numero, end= ' ')
            contar_numero += passo
        print(f"-------- Início: {inicio} até {fim} de {passo} a {passo}")
    else:
        contar_numero = inicio
        
        while contar_numero >= fim:
            print(contar_numero, end=' ')
            contar_numero -= passo
        print(f"-------- Início: {inicio} até {fim} de {passo} a {passo}")
            
        
        
contar(10,0,1)
contar(1,10,1)
linha()
numero_inicial = int(input("Digite um número: "))
numero_final = int(input("Até que número: "))
numero_passo = int(input("Digite um passo"))

contar(numero_inicial, numero_final, numero_passo)

