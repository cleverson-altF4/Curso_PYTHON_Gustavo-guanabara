from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.total = 1

        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total.")

    def avancarPaginas(self, total):
        for i in range(total):

            if i >= self.paginas:
                print(f"O livro termina na página {self.paginas}", end= " ")
                break
            else:
                print(f"pag {i + 1}", end=' ')
                sleep(1)
                total += 1

        print(f"Você avançou {i+1} e agora está na página {total}")


li1 = Livro("Harry Potter", 20)
li1.avancarPaginas(5)