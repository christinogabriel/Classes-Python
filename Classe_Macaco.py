class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.estomago = []

    def comer(self, alimento):
        self.estomago.append(alimento)

    def verBarriga(self):
        return self.estomago

    def digerir(self):
        if self.estomago:
            self.estomago.pop(0)  # Digere o primeiro item consumido


macaco1 = Macaco("Chico")
macaco2 = Macaco("Zé")

# Alimentando macacos
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco2.comer("Laranja")

# Verificando estômago
print("Estômago do Chico:", macaco1.verBarriga())
print("Estômago do Zé:", macaco2.verBarriga())

# Digestionando alimentos
macaco1.digerir()
macaco2.digerir()
print("Estômago do Chico após digerir:", macaco1.verBarriga())
print("Estômago do Zé após digerir:", macaco2.verBarriga())
