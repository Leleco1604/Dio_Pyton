class Pessoa:
    def __init__(self,nome = None ,idade = None):
        self.nome = nome
        self.idade = idade

    @classmethod  #transforma esse cara em um método de classe, e por isso e vez de colocarmos (self, ano, mes, dia, nome ), colocamos (cls, ano, mes, dia, nome):
    def criar_apartir_data_nascimento_(cls, ano, mes, dia, nome ):
        idade = 2023 - ano 
        return cls(nome, idade)


    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18 


# p = Pessoa("Leonardo", 20 )
# print(p.nome, p.idade)

p = Pessoa.criar_apartir_data_nascimento_(2003,4,16, "Leonardo" )
print (p.nome, p.idade)


print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
