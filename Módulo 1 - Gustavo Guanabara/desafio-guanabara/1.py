#letra maiuscula
nome = str(input("Nome: "))

letra_maiuscula = nome.upper()
print(f"Letras maiúsculas {letra_maiuscula}")

letra_minuscula = nome.lower()
print(f"Letras minúscula {letra_minuscula}")

total_letras = len(nome.replace("", ""))
print(f"Total de letras do {nome} é {total_letras}")#total de letras

primeiro_nome = nome.split()[0]
print(f"Primeiro nome de {nome} é {primeiro_nome}") #pega o primeiro nome 