class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mudarCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor


bola = Bola("Azul", 30, "Couro")
print("Cor inicial da bola:", bola.mostraCor())

bola.mudarCor("Vermelho")
print("Cor nova da bola:", bola.mostraCor())