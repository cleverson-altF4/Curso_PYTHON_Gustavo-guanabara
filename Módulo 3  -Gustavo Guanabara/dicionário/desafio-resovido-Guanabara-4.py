jogador = {}
gol = []
jogador['nome'] = str(input("Nome do jogador: ")).strip()
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(jogador['partidas']):
    gol.append(int(input(f"Quantos gols {jogador['nome']} fez? ")))
    
jogador['gol'] = gol
jogador['total'] = sum(gol)

print(jogador)

print("-"*35)

for k, v in jogador.items():
    print(f"{k}: ------ {v}")
    
print("-"*35)

print(f"O jogador {jogador['nome']} jogou {(jogador['partidas'])} partidas")

for i, valor in enumerate(jogador['gol']):
    print(f" Na partida {i+1} fez {valor} gols")
print(f"Foi um total de {sum(jogador['gol'])} gols")