from time import sleep
def maior(*numero):
    
    print("\n Números analisados")
    
    maior = contador = menor = 0
    
    for valor in numero:
        print(f"{valor}", end=' ', flush=True)
        sleep(0.5)
        
        if contador == 0:
            maior = menor = valor
        else:
            if valor > maior:
                maior = valor
            else:
                if valor < menor:
                    menor = valor
        contador += 1
    print(f"Total de números analisados: {contador}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    
    
    
maior(0,2,3,4,5)
maior(1,6,8)
maior(1,9)
maior()