#Leia uma palavra do usuário.
#Converta para minúsculas.
#Inicialize contador = 0.
#Para cada caractere na palavra, se for vogal (a, e, i, o, u), incremente contador.
#Imprima o total de vogais.

palavra = str(input("Digite uma palavra: ")).lower()
contador = 0
vogais = 'aeiou'

for caractere in palavra:
    if caractere in vogais:
        contador += 1

print("Números de vogais: {}".format(contador))

