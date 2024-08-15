class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  # km por litro
        self.nivel_combustivel = 0  # começa com o tanque vazio

    def adicionarGasolina(self, quantidade):
        self.nivel_combustivel += quantidade

    def andar(self, distancia):
        combustivel_necessario = distancia / self.consumo
        if combustivel_necessario > self.nivel_combustivel:
            print("Combustível insuficiente para percorrer a distância.")
            distancia_possivel = self.nivel_combustivel * self.consumo
            self.nivel_combustivel = 0
            print(f"O carro andou {distancia_possivel:.2f} km e ficou sem combustível.")
        else:
            self.nivel_combustivel -= combustivel_necessario
            print(f"O carro andou {distancia} km.")

    def obterGasolina(self):
        return self.nivel_combustivel

# Exemplo de uso
meuFusca = Carro(15)  # 15 km por litro
meuFusca.adicionarGasolina(20)  # abastece com 20 litros
meuFusca.andar(100)  # anda 100 km
print(f"Combustível restante no tanque: {meuFusca.obterGasolina():.2f} litros")
