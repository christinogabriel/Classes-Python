class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50
        self.saude = 100
        self.idade = 1

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def alimentar(self, quantidade):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.tedio -= tempo
        if self.tedio < 0:
            self.tedio = 0

    def humor(self):
        return (self.fome + self.tedio) / 2

    def __str__(self):
        return f"Bichinho: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}, Saúde: {self.saude}, Idade: {self.idade}"

# Exemplo de uso
bichinho = BichinhoVirtual("Tammy")
bichinho.alimentar(30)
bichinho.brincar(20)
print(bichinho)
