#Faça um programa que leia o sexo, mas so aceite os valores "M" ou "F", caso contrário
#peça a digitação novamente até ter um valor correto

sexo = str(input("Digite o seu sexo M/F: ")).strip().upper()[0]
print(sexo)
while sexo not in 'MfFm' :
    sexo = str(input("Dados inválidos, digite novamente: ")).strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso!")

