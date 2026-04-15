#faça um programa que tenha uma função chamada contador() que receba 3 parâmetros, INICIO, FIM, PASSO e realize uma contagem 

#Seu programa tem que realizar 3 contagens através da função criada

#A) de 1 até 10, de 1 em 1
#B0 de 10 até 0, de 2 em 2
#Uma contagem personalizado 
from time import sleep

def linha():
    print("-"*55)
    
    
def contar(inicio, fim, passo):
    contagem = inicio
    
    if inicio < fim:
        if passo == 0:
            passo += 1
            
        if passo < 0:
            passo *= -1
            
        
        while contagem < fim:
            print(contagem, end=' ', flush=True)
            contagem += passo
            sleep(0.5)
        print(f"------ início: {inicio} até {fim} de {passo} à {passo}")
    else:
        contagem = inicio
        
        while contagem >= fim:
            print(contagem, end=' ', flush=True)
            contagem -= passo
        print(f"------ início: {inicio} até {fim} de {passo} à {passo}")
            

contar(1,10,1)
contar(10,1,2)

inicial = int(input("Digite 1 número: "))
final = int(input("Digite até qual número final: "))
passando = int(input("Digite um número que passa de quanto e quanto: "))

contar(inicial, final, passando)