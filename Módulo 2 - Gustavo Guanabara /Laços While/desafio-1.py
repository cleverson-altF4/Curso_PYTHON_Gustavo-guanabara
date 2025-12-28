#Faça um programa que leia o sexo, mas so aceite os valores "M" ou "F", caso contrário
#peça a digitação novamente até ter um valor correto

sexo = str(input("Digite o seu sexo M/F: ")).strip().lower()

while sexo not in ['m', 'f']:
    print("Erro de digitação, tente novamente\n")
    print("Use apenas M/F\n")
    sexo = str(input("digite novamente: "))
    
print("Agora sim está correto")