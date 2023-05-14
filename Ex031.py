distancia = float(input('Qual é a distância da Viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
   preço = distancia *0.45
print('O valor da sua passagem é {}'.format(preço))