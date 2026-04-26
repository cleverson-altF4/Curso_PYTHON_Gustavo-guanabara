def aumentar(preco, taxa):
    resultado = preco + (preco * taxa / 100)
    return resultado


def diminuir(preco, taxa):
    resultado = preco - (preco - taxa / 100)
    return resultado


def dobro(preco):
    resultado = preco * 2
    return resultado


def metade(preco):
    resultado = preco / 2
    return resultado