#Peça o nome completo do usuário e mostre:
#O primeiro nome
#O último nome
#Quantas letras tem o nome completo (sem espaços)
# Solicita o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")
partes_nome = nome_completo.split()

primeiro_nome = partes_nome[0]

ultimo_nome = partes_nome[-1]

total_letras = len(nome_completo.replace(" ", ""))

print(f"Primeiro nome: ", primeiro_nome)
print(f"último nome: ", ultimo_nome)
print(f"Total de letras: ", total_letras)

