#Mostre apenas a primeira metade e a segunda metade de uma frase.

nome = input("Nome completo: ")

meio = len(nome) // 2

primeira_metade = nome[:meio]
segunda_metade = nome[meio:]

print(f"Primeira metade: ", primeira_metade)
print(f"Segunda metade: ", segunda_metade)