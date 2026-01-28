lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim'] #Cada nome tem um índice 0,1,2,3 que equivale a cada item
lanche[3] = 'Picolé' # adiciona o picolé no lugar do pudim
print(lanche)

#Para adicionar itens novos usa-se append

lanche.append('Toicim') #ele cria um quarto item e adiciona no final
print(lanche)

#para adicionar um item na posição que queira usa-se o Insert()
lanche.insert(0, 'Cachorro quente') 
print(lanche)

#apagar o elemento no modo simples
del lanche[3]
print(lanche)

#apagar usando o  com o elemento pop() ele apaga o último da lista
lanche.pop()
print(lanche)

#Apagar usando o pop() com o um parâmetro
lanche.pop(3)
print(lanche)

#apagar usando o remove() e nele você usa como parâmetro qual item apagar tipo:
lanche.remove('Suco')
print(lanche)

#caso for remover um item e ele não estiver na lista pode usar esse metódo
lanche.remove('Hambúrguer')
if 'Hambúrguer'in lanche:
    lanche.remove("Hambúrguer")
else:
    print("Lanche foi removido")
    
print(lanche)

