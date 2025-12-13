#calculadora usando função Def (fácil)
def calculadora(a, b, resultado):
    if resultado == '+':
        return a + b
    elif resultado == '-':
        return a - b
    elif resultado == '*':
        return a * b
    elif resultado == '/':
        if b == 0:
            print("Não é permitido número por zero")
        else:
            return a / b    
    else:
        print("Operação inválida")

print(calculadora(10, 5, '+'))
print(calculadora(10, 2, '/'))
print(calculadora(10, 5, '-'))
print(calculadora(10, 5, '*'))