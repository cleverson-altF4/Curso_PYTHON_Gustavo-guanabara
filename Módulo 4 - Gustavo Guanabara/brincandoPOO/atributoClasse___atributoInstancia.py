class carro:
    rodas = 4

    def __init__(self, modelo):
        self.modelo = modelo

carr1 = carro("Uno")
carr2 = carro("Fiat")

print(carr1.rodas, carr2.rodas)
carr1.rodas = 6

print(carr1.rodas, carr2.rodas)
