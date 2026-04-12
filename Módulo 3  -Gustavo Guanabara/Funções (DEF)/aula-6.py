#faça um programa que tenha uma função chamada contador() que receba 3 parâmetros, INICIO, FIM, PASSO e realize uma contagem 

#Seu programa tem que realizar 3 contagens através da função criada

#A) de 1 até 10, de 1 em 1
#B0 de 10 até 0, de 2 em 2
#Uma contagem personalizado 
from time import sleep

def linha():
    print("-"*55)
    

def contador(inicio, fim, passo):
    cont = inicio
    if inicio < fim:
        
        if passo < 0:
            passo *= -1
            
        if passo == 0:
            passo += 1
            
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont += passo
        
        print(f"   (Iniciou com {inicio} até {fim} de {passo} a {passo})")
        linha()
    else:
        cont = inicio
        
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont -= passo
        print(f"   (Iniciou com {inicio} até {fim} de {passo} a {passo})")
        linha()
    
        
linha()
contador(1,10,1)
contador(10,0,2)

inicial = int(input("início: "))
final = int(input("Fim:      "))
passando = int(input("Passo: "))
linha()
contador(inicial,final,passando)
