#Crie uma classe Retangulo com largura e altura. Adicione métodos area() e perimetro().


class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return (self.largura + self.altura) * 2



retang = Retangulo(4,6)
retang2 = Retangulo(10,43)
perime = Retangulo(10,5)

print(retang.area())
print(retang2.area())
print(perime.perimetro())



