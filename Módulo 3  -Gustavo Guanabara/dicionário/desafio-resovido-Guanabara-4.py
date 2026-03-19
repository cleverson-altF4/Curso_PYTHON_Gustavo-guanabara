jogador = {}
gol = []
jogador['Nome'] = str(input("Nome do jogador: ")).strip()
jogador['partidas'] = int(input(f"Quantos partidas {jogador['Nome']} fez? "))

for i in range(jogador['partidas']):
    gol.append(int(input(f"Quantos gols {jogador['Nome']} fez? ")))
    
jogador['gols'] = gol
jogador['total'] = sum(gol)

print('-'*40)

for k, c in enumerate(jogador.items()):
    print(f"{k+1} ________ {c}")
    
print("-"*40)

for i in jogador.items():
    print(f"{i}")
    
print("-"*40)

print(f"A quantidade de gols que {jogador['Nome']} fez foi {jogador['gols']}")
print(f"O total de gols na temporada foi {jogador['total']} gols no ano.")

for i, valor in enumerate(jogador['gols']):
    print(f"{i+1} _______{valor} gols")