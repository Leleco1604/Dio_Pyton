class conta:
    def __init__(self, nro_agencia, saldo = 0):
        self._saldo = saldo       # O "_" informar que o saldo é privado
        self.nro_agencia = nro_agencia

    def depositar(self,valor):
        # ...
        self._saldo += valor


    def sacar(self,valor):
        # ...
        self._saldo -= valor   


conta = conta("001", 100)
print(conta.nro_agencia)