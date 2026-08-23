from rich import print
from rich.panel import Panel

class Churrasco:
    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.quantidade = quantidade
        self.preco = 82.40
        self.consumo = 400


    def analisar(self):
        gramas = self.quantidade * self.consumo
        kilos = gramas / 1000
        valor = kilos * self.preco
        porPessoa = valor / self.quantidade
        print(Panel(f"Analisando o {self.titulo} com {self.quantidade} convidados "
                    f"Cada Participante comerá 0.4g cada KG custa R$:{self.preco} reais"
                    f" Recomendo comprar R$:{gramas}"
                    f" Cada pessoa pagará {porPessoa} para participar", width=80, title= f"{self.titulo}"))

        return porPessoa




carne = Churrasco("Churrasco de amigos", 100)
print(carne.analisar())