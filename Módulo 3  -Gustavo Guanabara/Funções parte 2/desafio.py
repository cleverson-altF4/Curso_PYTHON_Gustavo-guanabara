from datetime import date

def voto(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    
    if idade < 16:
        return f'Fulano tem {idade} anos: Não vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Fulano tem {idade} anos: Voto opcional'
    else:
        return f'Fulano tem {idade} anos: Voto obrigatório'
    
ano_nascimento = int(input("Digite a sua idade: "))
print(voto(ano_nascimento))
