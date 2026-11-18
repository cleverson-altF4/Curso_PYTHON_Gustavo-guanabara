class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def __str__(self) -> str:
        return f"{self.modelo} | {self.cor}"


    def __repr__(self) -> str:
        return f"Modelo = {self.modelo} | Cor= {self.cor}"

car = carro("Uno", "Preto")

print(repr(car))
print(car)