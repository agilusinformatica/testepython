class Pessoa:
    nome = None
    idade = None
    altura = None
    limite = 0
    __saldo = 0

    def __init__(self, nome, idade):
        self.nome = nome
        if idade < 18:
            raise ValueError('Idade inválida, garotão')
        self.idade = idade

    def deposito(self, valor):
        self.__saldo += valor
    def saque(self, valor):
        if valor > self.__saldo + self.limite:
            raise ValueError('Saldo insuficiente, seu pobre e lascado')
        self.__saldo -= valor
    def set_limite(self, limite):
        self.limite = limite

    def saldo(self):
        return self.__saldo


cliente = Pessoa('Felippe', 39)
cliente.set_limite(1000)
cliente.deposito(1000)
cliente.saque(2500)

print(cliente.saldo())
