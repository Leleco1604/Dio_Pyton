def area(lar, comp):
    area = lar * comp
    print("-"*30)
    print('LARGURA (m) = {lar}')
    print('COMPRIMENTO (m) = {comp}')
    print (f'A área do terreno é {area}')
    print("-"*30) 

lar = float(input("Qual é a largura do terreno?"))
comp = float(input("Qual é o comprimento do terreno?"))

area(lar ,comp)
