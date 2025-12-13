nome = str(input("Digite seu nome: ")).strip()
print(f"Maiúsculos {nome.upper()}")
print(f"Minúsculos = {nome.lower()}")
print(f"Quantas letras {len(nome) - nome.count(' ')}")
separar = nome.split()
print(f"seu primeiro nome é {separar[0]} e a quantidade de letras são {len(separar[0])}")      

















