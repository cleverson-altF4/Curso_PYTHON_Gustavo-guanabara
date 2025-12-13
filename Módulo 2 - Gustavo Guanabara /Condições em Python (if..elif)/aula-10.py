print("\n#~~~~~~~~~ Compras ~~~~~~~~~#\n")
valor = float(input("Digite o valor: "))
print("\n#~~~~~~~~ Formas de pagamento ~~~~~~~~#\n")
print('''
1 - pagamento a vista/cheque      
2 - à vista no cartão
3 - à vista no cartão 3x ou mais 
4 - sair''')
opcao = int(input("Digite a opção desejada: "))


if opcao == 1:
    total = valor - (valor * 10 / 100)
    print(f"O valor à vista será R$ {valor} reais com o desconto de {total:.2f} reais")
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print(f"O valor à vista no cartão com 5% de desconto {total:.2f} reais")
elif opcao == 3:
    total = valor + (valor * 20 / 100)
    print(f"A vista 3x ou mais no cartão é de {total:.2f} reais")
elif opcao == 4:
    print("Sair do programa")
    