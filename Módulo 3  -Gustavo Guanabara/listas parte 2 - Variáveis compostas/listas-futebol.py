#Passo a passo (iniciante) usando apenas listas Use este projeto com a regra didática mais comum:

#1º ao 6º = Libertadores
#7º ao 12º = Sul-Americana
#17º ao 20º = Rebaixados (Z-4)
#1º ao 4º = G-4 (parte de cima da Libertadores)

tabela = []
inicio = 0
quantidade = 20 # 20 times
print("-"*40)
print("       Campeonato Brasileiro      ")
print("-"*40)

while inicio <= quantidade:
    nome = str(input("Time: ")).strip()
    pontos = int(input("Pontos: "))
    vitorias = int(input("Vitorias: "))
    saldo = int(input("Saldo de gols: "))
    
    time = [nome, pontos, vitorias, saldo]
    tabela.append(time)
    inicio += 1
    
#praticar  Buble Sort    
for i in range(len(tabela)):
    for j in range(i + 1, len(tabela)):
        if tabela[i][1] < tabela[j][1]:
           temporario = tabela[i]
           tabela[i] = tabela[j]
           tabela[j] = temporario
    
    
print(f"{'J':>2}|{'Time':>15}|{'Pon':>3}|{'V':>3}|{'S':>3}| Situação")
print("-"*45)

for posicao in range(len(tabela)):
    colocacao = posicao + 1

    if colocacao <= 4:
        situacao = 'G4'
    elif colocacao <= 6:
        situacao = 'Libertadores'
    elif colocacao <= 12:
        situacao = 'Sul-Americano'
    elif colocacao >= 17:
        situacao = 'Rebaixamento'
    else:
        situacao = ''
        
    print(f"{colocacao:>2}|{tabela[posicao][0]:>15}|{tabela[posicao][1]:>3}|{tabela[posicao][2]:>3}|{tabela[posicao][3]:>3}| {situacao}")

    


