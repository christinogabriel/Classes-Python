class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        return f"Ponto({self.x}, {self.y})"

    def calcular_centro(self, outro_ponto):
        centro_x = (self.x + outro_ponto.x) / 2
        centro_y = (self.y + outro_ponto.y) / 2
        return Ponto(centro_x, centro_y)

class Retangulo:
    def __init__(self, largura, altura, vertice_inferior_esquerdo):
        self.largura = largura
        self.altura = altura
        self.vertice_inferior_esquerdo = vertice_inferior_esquerdo
        self.vertice_superior_direito = Ponto(vertice_inferior_esquerdo.x + largura, vertice_inferior_esquerdo.y + altura)

    def encontrar_centro(self):
        return self.vertice_inferior_esquerdo.calcular_centro(self.vertice_superior_direito)

    def imprimir_centro(self):
        centro = self.encontrar_centro()
        print(f"O centro do retângulo está em {centro.imprimir()}")


ponto_inicial = Ponto(0, 0)
retangulo = Retangulo(4, 6, ponto_inicial)

# Imprimir o centro do retângulo
retangulo.imprimir_centro()
