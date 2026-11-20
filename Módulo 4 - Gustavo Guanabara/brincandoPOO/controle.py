from time import  sleep
from traceback import print_tb


class TV:
    volumeMax = 100
    canalMax = 20

    def __init__(self, marca):
        self.marca = marca
        self.volume = 10
        self.ligada = False
        self.canal = 1

    def __str__(self) -> str:
        if not self.ligada:
            return f"{self.marca} | Desligada"
        else:
            return f"{self.marca} | Ligada"


    def ligarTV(self):
        self.ligada = True
        print('''
            Ligando Televisão
                ''')
        sleep(1.5)
        print(f"{self.marca} - Ligada")

    def desligarTV(self):
        self.ligada = False
        print('''
            Desligando Televisão
               ''')
        sleep(1.5)
        print(f"{self.marca} - Desligada")

    def aumentarVolume(self):
        if not self.volume:
            print("")
            return

        if self.volume > self.volumeMax:
            print(f"Volume está no máximo")

        self.volume += 1

    def diminuirVolume(self):
        if not self.volume:
            print("")
            return

        if self.volume <= 0:
            print(f"Volume já está no mínimo")

        self.volume -= 1



    def mudarCanal(self, opcao):
        if not self.canal:
            print("TV desligada")
            return

        if opcao < 1 or opcao > self.canalMax:
            print(f"Selecione o canal existente | {self.canal} até {self.canalMax}")

        self.canal = opcao

        if opcao == 9:
            print("SBT")
        elif opcao == 11:
            print("Globo")
        elif opcao == 13:
            print("Record")
        else:
            print(opcao)



televisao = TV("LG")
televisao.ligarTV()
televisao.aumentarVolume()
print(televisao.volume)
televisao.mudarCanal(-1)
