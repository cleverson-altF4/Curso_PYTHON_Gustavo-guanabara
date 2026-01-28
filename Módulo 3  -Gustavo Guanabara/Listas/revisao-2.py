
#Criar uma lista usando for - Lembrando que o range ele já cria uma estrutura já ordenada de forma crescente
print("*"*50)
print()
valores = list(range(4,11)) 
print(f"Uma estrutura já ordenada usando Range = {valores}")

print("*"*50)
print()
#Criando um elemento fora de ordem e para deixar ordenado usa o sort
valores = [8,4,5,3,4,6,5, ] 
valores.sort()
print("Ordenado usando sort()= {}".format(valores))
print("*"*50)
print()

#criando um elemento com valores ao contrário
valores = [8,4,5,3,4,6,5]
valores.sort(reverse=True)
print(f"Não ordenado usando Sort(reverse=True) = {valores}")

print("*"*50)
print()

#Saber o tamanho da lista
valores = [1,4,8,9,7,5,3,1,0]
print(f"QUANTIDA")