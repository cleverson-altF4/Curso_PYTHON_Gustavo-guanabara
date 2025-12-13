#cálculo básico
def somar(a, b):
    return a + b
print(f"Resultado da soma {somar(3, 2)}")


def subtrair(a, b):
    return a - b
print(f"Resultado da subtração {subtrair(3, 2)}")


def multiplicar(a, b):
    return a * b
print(f"Resultado da multiplicação = {multiplicar(3, 2)}")

def divisao(a, b):
    if b == 0:
        return "Divisão por zero não é permitido"
    return a / b
print(f"Resultado da divisão {divisao(3, 2)}")