from abc import ABC, abstractmethod 


class ControleRemoto(ABC):
    @abstractmethod 
    
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass 



class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligada!")

    def desligar(self):
        print("Desligar a TV... ") 
        print("Desligando!")      


class ContreArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando ar condicionado...")
        print("Desligado!")



controle = ControleTV()
controle.ligar()    
controle.desligar()


controle = ContreArCondicionado
controle.ligar()
controle.desligar()

