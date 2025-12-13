#Dada a palavra “Programação”:
#Mostre o total de letras
#Mostre do índice 3 até o 8
#Mostre apenas as vogais
#Mostre a palavra ao contrário

nome = str(input("Digite: "))
print(f"Total de letras {len(nome)}")
print(f"Índice 3 até o 8 {nome[3:8]}")

vogais = ''
for total in nome:
    if total.lower() in 'aeiou':
        vogais += total
        
print(f"Vogais em {vogais}")

print(f"nome {nome} ao contrário {nome[::-1]}")