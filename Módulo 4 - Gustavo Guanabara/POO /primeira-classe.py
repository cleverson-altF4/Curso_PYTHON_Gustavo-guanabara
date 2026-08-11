#Crie uma classe Pessoa com nome e idade. Adicione um método
# apresentar() que retorne "Olá, meu nome é {nome} e tenho {idade} anos."
from FuncoesTutorial.tutorial_funcoes import titulo


#Crie uma classe Livro com titulo, autor e paginas. Adicione um método
# resumo() que exiba as informações formatadas.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def apresentar(self):
        return print(f"Olá meu nome é {self.nome} e tenho {self.idade} anos")


fulano = Pessoa("Clevison", 31)
fulano.apresentar()

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas



    def resumo(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")

livros1 = Livro("Matrix", "Neo", 220)
livros2 = Livro("Cigano", "Beltrano", 100)

biblioteca = (livros1, livros2)

for i in biblioteca:
    i.resumo()