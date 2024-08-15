class Quadrado:
    def __init__(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado

    def mudarValorLado(self, novo_lado):
        self.tamanho_do_lado = novo_lado

    def retornarValorLado(self):
        return self.tamanho_do_lado

    def calcularArea(self):
        return self.tamanho_do_lado ** 2


quadrado = Quadrado(4)
print("Lado do quadrado:", quadrado.retornarValorLado())
print("Área do quadrado:", quadrado.calcularArea())

quadrado.mudarValorLado(5)
print("Novo lado do quadrado:", quadrado.retornarValorLado())
print("Nova área do quadrado:", quadrado.calcularArea())