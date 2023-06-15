# Self é uma referencia para o objeto, self é a instancia do objeto que foi passado 


# def __init__(self, cor,modelo,ano,valor  ):
#         self.cor = cor
#         self.modelo = modelo
#         self.ano = ano
#         self.valor = valor 


# # def __init__(self, cor,modelo,ano,valor  ): é um metodo construtor para colocarmos as carac do objeto,
# que no caso é (b1)

class bicicleta:
    def __init__(self, cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor 
  
  #Essas funçoes a seguir são metodos onde o objeto b1(bicicleta), pode realizar.
    def buzinhar(self):    
        print("Plim plim...")

    def parar(self):
        print("Parando bicleta...")
        print("Bicleta parada...")   

    def correr(self):
        print("Vrumm...")         

    # def __str__(self):
    #     return f"Bicicleta: cor= {self.cor}, modelo= {self.modelo}, ano= {self.ano}, valor= {self.valor}"
    

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"


b1 = bicicleta("Vermelha", "caloi", 2003, 600)        
b1.buzinhar()
b1.correr()
b1.parar()


b2 = bicicleta("verde", "monark", 2000, 189)
print(b2)
b2.correr()
