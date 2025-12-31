
while True:
    primeiro_termo = int(input("Digite o primeiro termo da PA: "))
    razao = int(input("Digite a razão: "))
    
    termo_atual = primeiro_termo
    contador = 0 # zero
    
    print(f"os 10 primeiro termos são = {termo_atual} números da PA", end= ' ')
    contador += 1 # conto
    
    
    while contador < 10:
        termo_atual = termo_atual + razao
        contador += 1
        print(f"{termo_atual}", end= ' ')
    print('\n')
        
    
    continuar = input("Deseja continuar: S/N: ").strip().lower()
    if continuar == 'n':
        break