class TV:
    VolumeMAX = 100
    CanalMAX = 10
    def __init__(self, marca):
        self.marca = marca
        self.volume = 10
        self.canal = 1
        self.ligada = False

    def __str__(self) -> str:
       if not self.ligada:
           return f"Tv {self.marca} - Desligada"
       else:
           return f"Tv {self.marca} - Ligada"

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def aumentarVolume(self):
        if not self.ligada:
            print("TV está desligada")
            return

        if self.volume >= self.VolumeMAX:
            print("O volume está no máximo")
            return

        self.volume += 1

    def diminuirVolume(self):
        if not self.ligada:
            print("TV está desligada")
            return

        if self.volume <= 0:
            print("O volume está no mínimoo")
            return

        self.volume -= 1

    def mudarCanal(self, numero):
        if not self.canal:
            print(f"TV está desligada")
            return

        if numero < 1 or numero > self.CanalMAX:
            print(f"Canal inválido, escolha de 1 a {self.CanalMAX}")
            return

        self.canal = numero


tv = TV("LG")
tv.mudarCanal(5)       # avisa: desligada
print(tv.canal)        # 1

tv.ligar()
tv.mudarCanal(1)       # válido, sem aviso
tv.mudarCanal(7)
tv.mudarCanal(3)
print(tv.canal)        # 3

tv.mudarCanal(50)      # inválido
print(tv.canal)        # continua 3
