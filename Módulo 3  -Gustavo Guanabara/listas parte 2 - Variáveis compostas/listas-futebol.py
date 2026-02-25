#Passo a passo (iniciante) usando apenas listas Use este projeto com a regra didática mais comum:

#1º ao 6º = Libertadores
#7º ao 12º = Sul-Americana
#17º ao 20º = Rebaixados (Z-4)
#1º ao 4º = G-4 (parte de cima da Libertadores)

tabela = []
inicio = 0
quantidade = 1 # 20 times
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
    
print(f"{'J':>2} | {'Time':>10} | {'V':>3} | {'S':>3} |")
for posicao, jogos in enumerate(tabela):
    print(f"{posicao + 1:>2} | {jogos[0]:>10} | {jogos[1]:>3} | {jogos[2]:>3} |")

    


