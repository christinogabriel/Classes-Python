class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

# Exemplo de uso
pessoa = Pessoa("João", 20, 70, 1.75)
print("Idade, Peso e Altura:", pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.envelhecer()
print("Nova idade, Peso e Altura após envelhecer:", pessoa.idade, pessoa.peso, pessoa.altura)
pessoa.engordar(5)
print("Peso após engordar:", pessoa.peso)
pessoa.emagrecer(3)
print("Peso após emagrecer:", pessoa.peso)
pessoa.crescer(0.1)
print("Altura após crescer:", pessoa.altura)
