#crie um programa que leia a idade e o sexo de várias pessoas cadastrada, o programa deverá perguntar se o usuário quer continuar ou não

# a - Quantas pessoas tem mais de 18 anos
# b - Quantos homens foram cadastrados
# c - Quantas mulheres tem menos de 20 anoswh
total18 = 0
total_homens = 0
total_mulheres = 0
print('*'*75)
print('*'*25, "Validação de idades", '*'*29)
while True:
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in ('M', 'F'):
        sexo = str(input("Sexo [M/F]: ")).strip().upper()
        if sexo == '':
            print("Apenas [M/F]")
    if idade > 18:
        total18 += 1   
        
    if sexo == 'M':
        total_homens += 1
        
    if idade < 20 and sexo == 'F':
        total_mulheres += 1
    
            
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar == '':
            print("Erro! Digite S ou N.")
        else:
            continuar = continuar[0]          
    if continuar == 'N':
        break

print(f"Total de pessoas com mais de 18 anos = {total18}")
print(f"Total de homens cadastrados = {total_homens}")
print(f"total de mulheres com menos de 20 anos = {total_mulheres}")
    
