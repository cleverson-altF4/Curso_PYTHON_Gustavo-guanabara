def aumentar(preco=0, taxa=0):
    '''Calcula o aumento de um determinado preço:
    retornando o resultado com ou sem formatação,
    param preço: o preço se quiser o reajuste
    param taxa: Qual é a porcentagem do aumento,
    param formato: quer uma saída formatada ou não?
    return o valor reajustado com ou sem formato
    '''
    
    resultado = preco + (preco * taxa / 100)
    return resultado 


def diminuir(preco=0, taxa=0):
    resultado = preco - (preco * taxa / 100)
    return resultado 


def dobro(preco=0):
    resultado = preco * 2
    return resultado 


def metade(preco=0):
    resultado = preco / 2
    return resultado 


def dinheiro(preco=0, cedula="R$"):
    return f"{cedula}{preco:.2f}".replace(".", ",")

def resumo(preco=0, taxa=10, taxaa=5):
    print("-"*35)
    print("Resumo do valor".center(35))
    print("-"*35)
    print(f"Preço analisado: \t{dinheiro(preco)}")
    print(f"O dobro do {dinheiro(preco)}: \t{dinheiro(dobro(preco))}")
    print(f"A metade do {dinheiro(preco)}: \t{dinheiro(metade(preco))}")
    print(f"A taxa de {taxa}% aumento:\t{dinheiro(aumentar(preco, taxa))}")
    print(f"A taxa de {taxaa}% reduzido: \t{dinheiro(diminuir(preco, taxaa))}")
    print("-"*35)