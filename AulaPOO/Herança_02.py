class animal:
    def __init__(self,nro_patas):
        self.nropatas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"



class mamifero(animal):
    def __init__(self,cor_pelo,**kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    
class ave(animal):
    def __init__(self,cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)



class gato(mamifero):
    pass


class onitorrinco(mamifero,ave):
    def __init__(self,cor_bico,cor_pelo,nro_patas):
        print(onitorrinco.__mro__)



        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)

gato = gato(nro_patas = 4,cor_pelo= "preto")
print(gato)


onitorrinco = onitorrinco(nro_patas = 2, cor_pelo = "Vermelho", cor_bico = "laranja")
print(onitorrinco)

# ave = ave(2, "verde")
# print(ave)