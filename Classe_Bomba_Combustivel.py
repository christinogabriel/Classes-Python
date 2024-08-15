class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos > self.quantidadeCombustivel:
            litros_abastecidos = self.quantidadeCombustivel
        self.quantidadeCombustivel -= litros_abastecidos
        return litros_abastecidos

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro
        if litros > self.quantidadeCombustivel:
            litros = self.quantidadeCombustivel
            valor_a_pagar = litros * self.valorLitro
        self.quantidadeCombustivel -= litros
        return valor_a_pagar

    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor

    def alterarCombustivel(self, novo_tipo):
        self.tipoCombustivel = novo_tipo

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade

# Exemplo de uso
bomba = BombaCombustivel("Gasolina", 5.00, 1000)

# Abastecendo por valor
litros = bomba.abastecerPorValor(50)
print(f"Abasteceu {litros} litros.")

# Abastecendo por litros
valor = bomba.abastecerPorLitro(10)
print(f"O valor a ser pago é R$ {valor:.2f}.")

# Alterando o valor do litro
bomba.alterarValor(6.00)
print(f"Novo valor por litro: R$ {bomba.valorLitro:.2f}")

# Alterando o tipo de combustível
bomba.alterarCombustivel("Etanol")
print(f"Novo tipo de combustível: {bomba.tipoCombustivel}")

# Alterando a quantidade de combustível na bomba
bomba.alterarQuantidadeCombustivel(2000)
print(f"Nova quantidade de combustível na bomba: {bomba.quantidadeCombustivel} litros")
