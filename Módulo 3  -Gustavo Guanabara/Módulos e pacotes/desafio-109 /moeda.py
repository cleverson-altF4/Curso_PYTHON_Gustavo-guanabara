def aumentar(preco=0, taxa=0, formato= False):
    resultado = preco + (preco * taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formato= False):
    resultado = preco - (preco * taxa / 100)
    return resultado


def dobro(preco=0, formato = False):
    resultado = preco * 2
    return resultado


def metade(preco=0, Formato = False):
    resultado = preco / 2
    return resultado 


def dinheiro(preco=0, cedula="R$"):
    return f"{cedula}{preco:.2f}".replace(".", ",")