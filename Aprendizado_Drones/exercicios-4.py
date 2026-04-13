# arquivos .txt e .json


#Salvando arquivo em .txt, "W" = write

with open("Log de voo", "w") as arquivo:
    arquivo.write("Voo iniciado\n")
    arquivo.write("Altitude: 50m\n")
    
    
#Lendo um arquivo "r" = read

with open("Log de voo", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
    
#Adicionando um novo texto "a" append (adiciona no final)

with open("Log de voo.txt", "a") as arquivo:
    arquivo.write("Pouso finalizado\n")
    
    
