def aumentar(preco=0, taxa=0):
    resultado = preco + (preco * taxa / 100)
    return resultado


def diminuir(preco=0, taxa=0):
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco=0):
    resultado = preco * 2
    return resultado


def metade(preco):
    resultado = preco / 2
    return resultado


def dinheiro(preco=0, cedula="R$"):
    return f"{cedula}{preco:.2f}".replace(".", ",")