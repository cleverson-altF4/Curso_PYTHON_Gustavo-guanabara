ficha = []

while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    
    continuar = ''
    while continuar not in ('S', 'N'):
        continuar = str(input("Deseja continuar? [sim/Não]: ")).strip().upper()
        if continuar == '':
            print("Espaço está em branco")
        else:
            continuar = continuar[0]
    if continuar == 'N':
        break
    
print("-"*30)
print(f'{"Nº":<4}{"Nome:":<10}{"Média:":>10}')
print("-"*30)
for i, aluno in enumerate(ficha):
    print(f'{i+1:<4}{aluno[0]:<10}{aluno[2]:>10.1f}')
    