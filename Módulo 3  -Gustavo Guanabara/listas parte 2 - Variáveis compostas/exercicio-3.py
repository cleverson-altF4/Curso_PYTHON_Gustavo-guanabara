galera = list()
dados = list()
maior = menor = 0
for i in range(0,3):
    dados.append(str(input("Digite o seu nome: ")))
    dados.append(int(input("Digite a sua idade: ")))
    galera.append(dados[:]) #[:] cria uma cópia
    dados.clear()
    
print("*"*30)

for i in galera: #Pecorre a lista
    if i[1] > 21: #indice[posição 0 nome e 1 idade]
        print(f"{i[0]} é maior de idade") #indice[0] pessoa com a idade tal
        
        maior += 1 # Quantidade de pessoas com maior de idade
    else:
        print(f"{i[0]} é menor de idade") #indice[o] a pessoa da lista
        menor += 1 # Quantidade de pessoas com menor de idade

print("*"*30)
        
print(f"Temos {maior} maior de idade")
print(f"Temos {menor} menor de idade")