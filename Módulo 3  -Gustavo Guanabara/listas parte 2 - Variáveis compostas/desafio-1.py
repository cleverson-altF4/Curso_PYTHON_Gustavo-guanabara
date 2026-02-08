lista_pessoas = list()
dados_da_lista = list()
pessoas_cadastradas = 0
maior_peso = menor_peso = 0


while True:
    dados_da_lista.append(str(input("Digite o seu nome: ")))
    dados_da_lista.append(float(input("Digite o seu peso: ")))
    lista_pessoas.append(dados_da_lista[:])
    dados_da_lista.clear()
    
    peso = lista_pessoas[-1][1]
    if len(lista_pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        
        if peso < menor_peso:
            menor_peso = peso            
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [S/N]: ")).strip().upper()
        if continuar == '':
            print("Não é permitido espaço vazio")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("-"*40)
    
pessoas_cadastradas = len(lista_pessoas)
print("\nTotal de pessoas cadastradas:", pessoas_cadastradas)
print("Maior peso:", maior_peso, "kg")
print("Menor peso:", menor_peso, "kg")

print("-"*40)
#laço percorre a lista de pessoas maior peso       
for i in lista_pessoas:
    if i[1] == maior_peso:
       print(f"{i[0]} tem {i[1]} kg")
            
    
#Laço percorre a lista de pessoas com menor peso
for i in lista_pessoas:
    if i[1] == menor_peso:
        print(f"{i[0]} tem {i[1]} kg")

    
    
