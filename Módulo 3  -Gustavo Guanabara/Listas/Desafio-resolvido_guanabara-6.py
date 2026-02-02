#Crie um programa que o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

#Nível intermediário

expressao = str(input("Digite uma expressão: "))
pilha = []

for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append()
            break
        
if len(pilha) == 0:
    print("Seu cálculo está correto")
else:
    print("falta um parênteses")