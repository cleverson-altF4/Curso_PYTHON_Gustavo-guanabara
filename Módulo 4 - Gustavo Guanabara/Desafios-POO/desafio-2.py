from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import box

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        print(Panel(f"-------------- {self.nome}---------- {self.preco} -----------------", title="Produto", width=30))


p1 = Produto("Arroz", 12.00)
p2 = Produto("Feijão", 12.00)
p1.etiqueta()
p2.etiqueta()