lista = []

print("-"*30)
print("      Sistema escolar    ")
print("-"*30)

while True:
    print('''
      1 - Cadastrar aluno
      2 - Mostrar todos os alunos
      3 - Mostrar alunos aprovados
      4 - Mostrar alunos reprovados
      5  - Sair''')
    print()
    
    opcao = int(input("Selecione a opção desejada: "))
   
    if opcao == 1:
         aluno = {}
         aluno['nome'] = str(input("Digite o seu nome: ")).strip()
         aluno['nota1'] = float(input("Nota: "))
         aluno['nota2'] = float(input("Nota: "))
         aluno['nota3'] = float(input("Nota: "))
         media = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3
         aluno['media'] = media
         
         lista.append(aluno)
         print("Aluno cadastrado com sucesso!")
    elif opcao == 2:
      if len(lista) == 0:
        print("Não há aluno cadastrado")
      else:
          print("\nLista completa\n")
          for i in range(len(lista)):
              aluno = lista[i]
              
              print(f"{i+1} - {aluno['nome']} | Nota 1: {aluno['nota1']:.2f} | Nota 2: {aluno['nota2']:.2f} | Nota 3: {aluno['nota3']:.2f} | Média: {aluno['media']:.2f}")
    elif opcao == 3:
      if len(lista) == 0:
        print("Não há aluno registrado")
      else:
        print("\nAlunos aprovados\n")
        for aluno in lista:
          if aluno['media'] >= 7:
            print(f"Aluno: {aluno['nome']} | Média: {aluno['media']:.2f}")
    elif opcao == 4:
      if len(lista) == 0:
        print("\nNão há aluno registrado\n")
      else:
        print("\nAlunos reprovados\n")
        for aluno in lista:
          if aluno['media'] < 7:
            print(f"Aluno: {aluno['nome']} | Média: {aluno['media']:.2f}")
    elif opcao == 5:
      if opcao == 5:
        print("\nSaindo do programa")
        break
      else:
        print("Inválido")