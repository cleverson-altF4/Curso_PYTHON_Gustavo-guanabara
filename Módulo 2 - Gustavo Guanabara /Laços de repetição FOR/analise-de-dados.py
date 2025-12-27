media = 0
soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher = 0

for p in range(1,5):
    print("#"*10, " {}° - Pessoa ".format(p),"#"*10)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("M/F: ")).strip().upper()
    soma_idade += idade
    
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1

media = soma_idade / 4
print("A média de idade do grupo é de {} anos.".format(media))
print("O homem mais velho do grupo tem {} anos e se chama {}".format(maior_idade_homem, nome_velho))
print("Ao total de mulheres com menos de 20 anos são ao total de {} ".format(total_mulher))



