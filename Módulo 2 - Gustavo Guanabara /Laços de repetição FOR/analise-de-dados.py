media = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher = 0
soma_idade = 0

for p in range(1,5):
    print("*"* 10, "Maioridade de idade", "*"* 10, "\n")
    nome = str(input("Digite o seu nome: ")).strip().upper()
    idade = int(input("Sua idade: "))
    sexo = str(input("Sexo M/F: ")).strip()
    soma_idade += idade

    if  p== 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1

media = soma_idade / 4
print(f"A média da idade do grupo é de {media} anos")
print(f"A pessoa mais velha do grupo é {maior_idade_homem} anos e o nome dele é {nome_velho}")
print("Ao total são {} mulheres com menos de 20 anos".format(total_mulher))
