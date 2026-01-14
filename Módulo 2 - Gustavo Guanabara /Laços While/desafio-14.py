#crie um programa que leia a idade e o sexo de várias pessoas cadastrada, o programa deverá perguntar se o usuário quer continuar ou não

# a - Quantas pessoas tem mais de 18 anos
# b - Quantos homens foram cadastrados
# c - Quantas mulheres tem menos de 20 anos
quantidade_pessoas = 0
quantidade_homens = 0
quantidade_mulheres = 0
quantidade_mais18 = 0
print('*'*75)
print()
print('*'*25, "Validação de idades", '*'*29)
print()
print('*'*75)


while True:
    idade = int(input("Digite a sua idade: "))
    sexo = str(input("Digite o seu sexo [M/F]: ")).strip().upper()
    
    if sexo not in ('M', 'F'):
        print('*'*75)
        print("\n\033[31mErro!\033[mDados incorretos, tente novamente\n")
        print('*'*75)
        continue
    
    quantidade_pessoas += 1
    
    if idade > 18:
        quantidade_mais18 += 1
    
    if sexo == 'M':
        quantidade_homens += 1
        
    if sexo == 'F' and idade < 20:
        quantidade_mulheres += 1
        
    continuar = str(input("Deseja continuar? [Sim ou Não]: ")).strip().upper()[0]
    if continuar == 'N':
        break

    
print("-"*50)
print(f"Total de pessoas cadastradas: {quantidade_pessoas}")
print(f"Pessoas com mais de 18 anos: {quantidade_mais18}")
print(f"Homens cadastrados: {quantidade_homens}")
print(f"Mulheres com menos de 20 anos: {quantidade_mulheres}")
print("-"*50)