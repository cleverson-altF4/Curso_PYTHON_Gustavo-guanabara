
def ficha(jogador='<Desconhecido>', gol=0):
    print(f"O jogador {jogador} fez {gol} gol(s) no campeonato")
    
    
    
jogador = str(input("Nome do jogador: ")).strip()
gol = input("Quantos gols? ")
 
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
    

if jogador == '':
    ficha(gol=gol)
else:
    ficha(jogador, gol)   
