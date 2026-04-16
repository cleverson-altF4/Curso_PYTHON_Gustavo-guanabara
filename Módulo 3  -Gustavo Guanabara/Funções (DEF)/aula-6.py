#faça um programa que tenha uma função chamada contador() que receba 3 parâmetros, INICIO, FIM, PASSO e realize uma contagem 

#Seu programa tem que realizar 3 contagens através da função criada

#A) de 1 até 10, de 1 em 1
#B0 de 10 até 0, de 2 em 2
#Uma contagem personalizado 
from time import sleep

def linha():
    print("-"*55)
    
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1 #Torna o passo em positivo
        
    if passo == 0:
            passo = 1
            
    linha()
    print(f"contagem {inicio} até o {fim} de {passo} em {passo}\n")
     
    if inicio < fim:   
        contador = inicio
        
        while contador <= fim:
            print(contador, end=' ', flush=True)
            sleep(0.3)
            contador += passo
        print("Fim")
    else:
        contador = inicio
        while contador >= fim:
            print(contador, end=' ',flush=True)
            sleep(0.3)
            contador -= passo
        print("Fim")
        

contador(1,10,1)
contador(10,0,2)
print("\nMeu código personalizado\n")

inicial = int(input("Digite um número: "))
fim = int(input("Digite o número final: "))
passando = int(input("Digite de quanto em quanto: "))
contador(inicial, fim, passando)