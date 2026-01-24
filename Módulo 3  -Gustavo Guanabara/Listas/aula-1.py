numero = [1,2,3,4,5,6]
numero[3] = 3
numero.append(4) # adicionando um numero usando append(7) e ele ficará na última posição
numero.sort() # números alinhados na ordem correta
numero.sort(reverse=True) # números de trás para frente
numero.insert(0,0) # O insert você escolhe a posição de onde quer deixar e adiciona um valor desejado que foi o 0
numero.pop() # ele irá apagar apenas o último número
numero.pop(3) # ele irá apagar o número 3 da lista
print(numero)
print(f"Essa lista tem {len(numero)} elementos")