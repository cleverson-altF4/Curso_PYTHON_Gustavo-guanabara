class livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano


    def descricao(self):
        print(f"O livro {self.titulo} foi escrito por {self.autor} em {self.ano}")


Livro1 = livro("Gladiador", "Riddley Scott", 2000)
Livro2 = livro("Matrix", "Lana Wachoowski", 1999)
Livro3 = livro("Game of thrones - Guerra dos tronos", "George R.R Martin ", 1996)

biblioteca = (Livro1, Livro2, Livro3)

for leitura in biblioteca:
    leitura.descricao()

