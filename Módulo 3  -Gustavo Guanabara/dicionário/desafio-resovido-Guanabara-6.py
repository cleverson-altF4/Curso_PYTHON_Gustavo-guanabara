time = []

while True:
    jogador = {}
    partida = []
    jogador['Nome']= str(input("Nome do jogador? ")).strip()
    total = int(input(f"Quantos partidas {jogador['Nome']} fez? "))
    
    
    for i in range(0, total):
        partida.append(int(input(f"Quantos gols {jogador['Nome']} fez? ")))
        
    jogador['gols'] = partida[:]
    jogador['total de gols'] = sum(partida)
    
    time.append(jogador.copy())
    
    while True:
        resposta = str(input("Deseja continuar? [Sim ou Não]: ")).upper()[0]
        if resposta in 'SN':
            break
        print("Digite corretamente [Sim ou Não]")
    if resposta == 'N':
        break
    
    
    print('-'*40)

print(f"{'Cod':>3} ",end='')
for posicao in jogador.keys():
    print(f"{posicao:<15}",end='')
print()
print('-'*40)
for keys, valor in enumerate(time):
    print(f"{keys + 1:>3}",end='') 
    for dados in valor.values():
        print(f" {str(dados):<15}", end='')    
    print()
    
    
#Dados para pegar a posição de cada jogador
print('-'*40)

while True:
    busca = int(input("Deseja coletar dados de qual jogador? [999 cancela]: "))
    
    if busca == 999:
        break
    
    if busca < 1 or busca > len(time):
        print(f"A busca {busca} não está na lista")
    else:
        print(f"\nRelatório completo\n")
        print(f"Busca por {time[busca-1]['Nome']}")
        
        for i, relatorio in enumerate(time[busca-1]['gols']):
            print(f"No {i+1}° jogo {relatorio}")