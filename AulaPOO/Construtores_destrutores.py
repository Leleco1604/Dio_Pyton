class cachorro:
    def __init__(self,nome,cor,acordado=True):
        print("Inicializando classe...")
        self.nome = nome 
        self.cor = cor 
        self.acordado = acordado 



    def falar(self):
        print("AU! AU!")

c = cachorro('Charpie', 'Preto')   
c.falar()        
