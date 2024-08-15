class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudarValorLados(self, novo_base, novo_altura):
        self.base = novo_base
        self.altura = novo_altura

    def retornarValoresLados(self):
        return self.base, self.altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


retangulo = Retangulo(4, 6)
print("Lados do retângulo:", retangulo.retornarValoresLados())
print("Área do retângulo:", retangulo.calcularArea())
print("Perímetro do retângulo:", retangulo.calcularPerimetro())

retangulo.mudarValorLados(5, 7)
print("Novos lados do retângulo:", retangulo.retornarValoresLados())
print("Nova área do retângulo:", retangulo.calcularArea())
print("Novo perímetro do retângulo:", retangulo.calcularPerimetro())
