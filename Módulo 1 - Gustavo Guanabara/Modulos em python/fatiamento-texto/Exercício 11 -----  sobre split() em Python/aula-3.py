#3. Contar quantos itens foram digitados

#Peça ao usuário para digitar nomes separados por vírgula e mostre quantos nomes ele digitou.

nome = input("Digite total de nomes: ")
virgula = nome.split(",")
total_nomes = len(virgula)
print(f"total de nomes digitados {total_nomes}")