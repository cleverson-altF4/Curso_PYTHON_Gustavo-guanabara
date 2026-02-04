lista = []

print("*"*40)
print("Menu de compras")
print('''
      [1] - Adicionar um produto
      [2] - Remover um produto
      [3] - Mostrar a lista de compras
      [4] - sair da lista''')
opcao = int(input("Selecione uma opção: "))

while True:
    lista.append(str(input("Anote a sua lista de compras: ")))
    

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja adicionar outro? [Sim ou Não]: ")).strip().upper()
        if continuar == '':
            print("Está vazio, digite novamente")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
    if '' in lista:
        lista.remove('')

        
        

        
for posicao, compras in enumerate(lista):
        print(f"{posicao + 1} = {compras}")
        


    
