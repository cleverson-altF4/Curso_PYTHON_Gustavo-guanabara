ficha = []

print("-"*50)
print("-------- Boletim com listas compostas --------")

while True:
    nome = str(input("Nome: ")).strip()
    nota_1 = float(input("Nota 1: "))
    nota_2 = float(input("Nota 2: "))
    media = (nota_1 + nota_2) / 2

    ficha.append([nome, [nota_1, nota_2], media])

    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [Sim/Não]: ")).strip().upper()
        if continuar == '':
            print("Espaço está em branco")
        else:
            continuar = continuar[0]

    if continuar == 'N':
        break

print("-"*50)
print(f"{'Nº':<4}{'Nome':<10}{'Média':>15}")

for i, aluno in enumerate(ficha):
    print(f"{i+1:<4}{aluno[0]:<10}{aluno[2]:>15.1f}")

print("-"*50)

while True:
    operacao = input("Mostrar notas de qual aluno? [999 interrompe]: ")

    if not operacao.isnumeric():
        print("Digite apenas números")
        continue
    
    operacao = int(operacao)
    
    if operacao == 999:
        print("Finalizando...")
        break
    
    if operacao >= 1 and operacao <= len(ficha):
        print(f"Aluno(a): {ficha[operacao - 1][0]} | Notas: {ficha[operacao - 1][1]}")
    else:
        print("Não foi encontrado nenhum aluno na lista")
