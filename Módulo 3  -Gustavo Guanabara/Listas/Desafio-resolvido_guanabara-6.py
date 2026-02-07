#Crie um programa que o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#Nível intermediário

expressao = str(input("Digite uma expressão: "))
parenteses = []

for simbolo in expressao:
    if simbolo == '(':
        parenteses.append("(")
    elif simbolo == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append()
            break
    
if len(parenteses) == 0:
    print("Seu cálculo está correto")
else:
    print("Está errado")