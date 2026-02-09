lista_pessoas = list()
dados_lista = list()
pessoas_cadastradas = 0
maior = menor = 0

while True:
    dados_lista.append(str(input("Digite o seu nome: ")))
    dados_lista.append(float(input("Digite o seu peso: ")))
    lista_pessoas.append(dados_lista[:])
    dados_lista.clear()
    
    peso = lista_pessoas[-1][1] # Pega a última pessoa da lista até o primeiro
    
    if len(lista_pessoas) == 1: #Se a quantidade de pessoas da lista for até o 1
        maior = menor = peso  #maior peso, menor peso e peso
    else:
        if peso > maior:
            maior = peso
        
        if peso < menor:
            menor = peso
            
            
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("deseja continuar? [Sim/Não]: ")).strip().upper()
        if continuar == '':
            print("Não é permitido espaços vazios")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("-"*40)

pessoas_cadastradas = len(lista_pessoas)
print(f"Temos {pessoas_cadastradas} pessoas cadastradas")
print(f"O maior peso = {maior}")
print(f"O menor peso = {menor}")

print("-"*40)

for i in lista_pessoas:
    if i[1] == maior:
        print(f"{i[0]} tem o maior peso que é {maior} kg")
        
        
for i in lista_pessoas:
    if i[1] == menor:
        print(f"{i[0]} tem o menor peso que é {menor} kg")
        
print("-"*40)