class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1


tv = TV()
print("Canal e Volume inicial:", tv.canal, tv.volume)
tv.mudarCanal(5)
print("Novo Canal:", tv.canal)
tv.aumentarVolume(50)
print("Volume após aumentar:", tv.volume)
tv.diminuirVolume(1)
print("Volume após diminuir:", tv.volume)
