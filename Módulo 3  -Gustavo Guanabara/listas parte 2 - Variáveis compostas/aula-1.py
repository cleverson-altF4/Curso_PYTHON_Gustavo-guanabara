#Estrutura de uma lista simples
dados = list()
dados.append("Clevison")
dados.append(31)
dados.append("Maria")
dados.append(49)
dados.append("cuca")
dados.append(25)
print(dados[0])
print(dados[1])


#Estruturas compostas
pessoas = []
pessoas.append(dados[:]) #Cópia de dados [:] fatiamento completo de uma estrutura de dados
print(pessoas)



#Estruturas com índices 
pessoas = [["Clevison",31], ["Maria", 49], ["Cuca", 25]]
print(pessoas[0][0]) #clevison
print(pessoas[1][1]) #49
print(pessoas[2][0]) #Cuca
print(pessoas[1]) #Maria, 49