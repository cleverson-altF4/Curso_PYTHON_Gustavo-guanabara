from rich import print
from rich.table import Table
from rich import box

tabela = Table(title="Clevison", box=box.SIMPLE_HEAD)

tabela.add_column("ID", justify="right", style="white", no_wrap=True)
tabela.add_column("Título", style="yellow")
tabela.add_column("Ano", justify="right",style="red")

tabela.add_row("1", "Gladiador", "1995")
tabela.add_row("2", "Gladiadorrrrrrrr", "1995")
tabela.add_row("3", "Gladiadorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", "1995")

print(tabela)