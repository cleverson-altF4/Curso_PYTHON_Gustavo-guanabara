from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.total = 1

        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Você está "
              f"agora na página {self.total}")

    def avancarPaginas(self, total):
        for i in range(total):
            print(f"pag{i+1}", end=' ')
            sleep(1)
            total += 1
        print(f"Você avançou {i+1} e agora está na página {total}")


li1 = Livro("Harry Potter", 20)
li1.avancarPaginas(5)
li1.avancarPaginas(5)