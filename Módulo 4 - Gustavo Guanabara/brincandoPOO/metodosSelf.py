#Método Self
class carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def aceleracao(self, quantidade):
        self.velocidade += quantidade

    def descrever(self):
        print(f"O modelo: {self.modelo} | Cor: {self.cor} | Velocidade: {self.velocidade} Km/h")


car1 = carro("Uno", "Azul")
car1.aceleracao(2)
car1.aceleracao(4)
car1.aceleracao(5)
car1.descrever()

