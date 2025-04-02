class Pessoa:
    nome = None
    idade = None
    altura = None
    __saldo = 0

    def __init__(self, nome, idade):
        self.nome = nome
        if idade < 18:
            raise ValueError('Idade inválida')
        self.idade = idade

    def deposito(self, valor):
        self.__saldo += valor
    def saque(self, valor):
        if valor > self.__saldo:
            raise ValueError('Saldo insuficiente, seu pobre e duro.')
        self.__saldo -= valor

    def saldo(self):
        return self.__saldo


cliente = Pessoa('Felippe', 39)
cliente.deposito(1000)
cliente.saque(800)

print(cliente.saldo())
