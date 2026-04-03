
time = []
while True:
    partidas = []
    jogador = {}
    jogador.clear()
    jogador['Nome'] = str(input("Nome do jogador? ")).strip()
    total = int(input(f"Quantas partidas {jogador['Nome']} fez? "))
    
    for contador in range(0, total):
        partidas.append(int(input(f"Quantos gols {jogador['Nome']} fez? ")))   
         
    jogador['gols'] = partidas[:] 
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    
    while True:
        resposta = str(input("Deseja continuar? S/N: ")).upper()[0]
        if resposta in 'SN':
            break
        else:
            print("Reponda corretamente")
    if resposta == 'N':
        break

print("-" * 45)
print(f"{'cod':>3} ", end='')
for i in jogador.keys():
    print(f"{i:<18} ", end='')
print()
print("-" * 45)
for keys, valor in enumerate(time):
    print(f"{keys+1:>3} ", end='')
    for dados in valor.values():
        print(f"{str(dados):<18} ", end='')
    print()
    

    
#Qual jogador você quer ver os dados?
while True:
    busca = int(input("Mostrar dados de qual jogador? [999] cancela: ")) 
    if busca == 999:
        break
    
    if busca < 1 or busca > len(time):
        print("Não há jogadores acima da busca")
    else:
        print("\nRelatório\n")

        print(f"Jogadores {time[busca - 1]['Nome']}")        
        
        for posicao, gols in enumerate(time[busca - 1]['gols']):
            
            print(f"Na {posicao + 1}° partida {time[busca - 1]['Nome']} fez {gols} gols")
        print("-"*45)


    