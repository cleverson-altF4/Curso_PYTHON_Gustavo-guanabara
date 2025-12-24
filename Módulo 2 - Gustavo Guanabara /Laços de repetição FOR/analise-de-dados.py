media = 0
soma_idade = 0
maior_idade_homem = 0
nome_velho = ''

for p in range(1,5):
    print("#"*10, " {}° - Pessoa ".format(p),"#"*10)
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("M/F: ")).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem += idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

media = soma_idade / 4
print(f"Média = {media} anos")
print(f"O homem mais velho tem {maior_idade_homem} anos e ele se chama {nome}")


