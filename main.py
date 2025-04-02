import start

class Cliente(start.Pessoa):
    agencia = ''

    def abertura_conta(self, deposito_inicial):
        self.deposito(deposito_inicial)
        print(f'Conta aberta com sucesso na agencia {self.agencia}')

    def saque(self, valor):
        super().saque(valor)
        print(f'Saque de {valor} realizado com sucesso')

    def __init__ (self, nome, idade, agencia):
        super().__init__(nome, idade)
        self.agencia = agencia

claudio = Cliente('Claudio', 45, '001')
claudio.abertura_conta(1654)
claudio.saque(200)
print(claudio.saldo())

