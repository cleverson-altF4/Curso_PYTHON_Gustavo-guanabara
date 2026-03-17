jogador = {}
gol = []
jogador['nome'] = str(input("Nome do jogador: ")).strip()
jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for i in range(jogador['partidas']):
    gol.append(int(input(f"Quantos gols {jogador['nome']} fez? ")))
    
jogador['gol'] = gol

print(jogador)

