#crie um programa que leia a idade e o sexo de várias pessoas cadastrada, o programa deverá perguntar se o usuário quer continuar ou não

# a - Quantas pessoas tem mais de 18 anos
# b - Quantos homens foram cadastrados
# c - Quantas mulheres tem menos de 20 anos
quantidade_pessoas = 0
quantidade_homens = 0
quantidade_mulheres = 0
mais_18 = 0

print("-"*50)
print('*'*18, "Fim do Programa", '*'*15)
print("-"*50)

while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    
    if sexo not in ('M', 'F'):
        print("-"*50)
        print("\nNão é permitido. Tente apenas [M ou F]")
        print("-"*50)
        continue
    
    quantidade_pessoas += 1
    
    if idade > 18:
        mais_18 += 1
        
    if sexo == 'M':
        quantidade_homens += 1
        
    if sexo == 'F' and idade < 20:
        quantidade_mulheres += 1
        
    
    continuar = input("Quer continuar? [Sim ou Não]: ").strip().upper()[0]
    if continuar == 'N':
        break
    
print("-"*50)
print(f"Total de pessoas cadastradas: {quantidade_pessoas}")
print(f"Pessoas com mais de 18 anos: {mais_18}")
print(f"Homens cadastrados: {quantidade_homens}")
print(f"Mulheres com menos de 20 anos: {quantidade_mulheres}")
print("-"*50)

    