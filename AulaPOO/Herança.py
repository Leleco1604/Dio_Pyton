class veiculo:
    def __init__(self,cor,placa,numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas


    def ligar_motor(self):
        print("Ligando motor ")


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"


class motocilcleta(veiculo):
    pass


class carro(veiculo):
    pass


class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def estar_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = motocilcleta("preta", "abc", 2)
# print(moto)
# moto.ligar_motor()

carro = carro("branco", "xde-500", 4)
# carro.ligar_motor()

caminhao = caminhao("roxo","lele-co34", 8, False)
# caminhao.ligar_motor()
# caminhao.estar_carregado()

print(moto)
print(carro)
print (caminhao)