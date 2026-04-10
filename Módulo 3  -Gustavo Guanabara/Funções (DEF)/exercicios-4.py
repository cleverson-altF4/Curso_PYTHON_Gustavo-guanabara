lista = []

def linha():
    print("-"*30)
    

def numeros_pares():
    while True:
        add_num = int(input("Adicione número na lista: "))
        print(f"Número {add_num} adicionado na lista")
        lista.append(add_num)
        
        linha()
        while True:
            resposta = str(input("Deseja continuar? ")).upper()[0]
            if resposta in 'SN':
                break   
        if resposta == 'N':
                break
            
     
numeros_pares()

linha()
print(f"\n Relatório \n")

if len(lista) == 0:
    print("Nâo há números na lista")
else:
    for numero in lista:
        if numero % 2 == 0:
            print(f"{numero}: par")
        else:
            print(f"{numero}: ímpar")
        

linha()
print(f"Lista completa: {lista}")
print(f"Total de números digitados: {len(lista)}")        
