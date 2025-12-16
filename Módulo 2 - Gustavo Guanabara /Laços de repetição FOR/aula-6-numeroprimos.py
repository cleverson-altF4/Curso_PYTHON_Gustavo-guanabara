from colorama import Fore, Back, Style, init
init(autoreset=True)

#print(Fore.RED + "Texto vermelho")
#print(Fore.GREEN + "Texto verde")
#print(Back.YELLOW + "Fundo amarelo")
#rint(Style.BRIGHT + "Texto em negrito")
#print(Style.RESET_ALL + "Texto normal")

numero = int(input("Digite um número: "))
total = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        print(Fore.GREEN + f"{i}",end= ' ')
        total += 1
    else:
 
        print(Fore.RED + f"{i}",end= ' ')

print(Style.BRIGHT + f"\n\33[m0 Total de número divísiveis por {numero} = {total} vezes")
if total == 2:
    print(Back.YELLOW + "Ele é um número primo")
else:
    print(Style.BRIGHT + "Ele não é primo")