class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def devolverNome(self):
        return self.nome

    def devolverSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        self.salario += self.salario * (percentualDeAumento / 100)


gabriel = Funcionario("Gabriel", 25000)
gabriel.aumentarSalario(10)
print(f"Novo salário de {gabriel.devolverNome()}: R$ {gabriel.devolverSalario():.2f}")
