teste = list() #variável teste
teste.append('Clevison') #Adiciona clevison na lista teste
teste.append(31) #Adiciona a idade 31 

galera = list() #variável galera
galera.append(teste[:]) #Adiiona a variável teste em galera em teste com a cópia [:]

teste[0] = 'Cuca' #Teste com índice 0
teste[1] = 25 #Teste com índice 1

galera.append(teste[:]) 
print(galera)