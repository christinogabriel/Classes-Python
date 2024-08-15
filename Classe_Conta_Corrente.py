class ContaCorrente:
    def __init__(self, numero_da_conta, nome_corrente, saldo=0):
        self.numero_da_conta = numero_da_conta
        self.nome_corrente = nome_corrente
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_corrente = novo_nome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")


conta = ContaCorrente(1234, "Gb", 100)
print("Saldo inicial:", conta.saldo)
conta.deposito(50)

print("Saldo após depósito:", conta.saldo)
conta.saque(30)

print("Saldo após saque:", conta.saldo)
conta.alterarNome("Gbzord")

print("Novo nome do correntista:", conta.nome_corrente)


