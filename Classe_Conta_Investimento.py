class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo_inicial = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicionarJuros(self):
        self.saldo_inicial += self.saldo_inicial * self.taxa_juros

    def obterSaldo(self):
        return self.saldo_inicial

# Exemplo de uso
conta = ContaInvestimento(1000.0, 0.10)

for conta in range(5):
    conta.adicionarJuros()

print(f"Saldo após 5 adições de juros: R$ {conta.obterSaldo():.2f}")
