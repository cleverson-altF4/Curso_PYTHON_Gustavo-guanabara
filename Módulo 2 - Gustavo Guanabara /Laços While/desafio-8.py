#crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição para sair. No final mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)
numero = soma = contador = 0
numero = int(input("Digite um número. (999 para sair): "))
while numero != 999:
    soma += numero
    contador += 1
    numero = int(input("Digite um número. (999 para sair): "))
print(f"A soma dos números foram {soma} e quantidade de vezes digitadas foram {contador}")