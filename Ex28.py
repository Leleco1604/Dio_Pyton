from random import randint
computador = randint( 0, 5) # faz o computador "Pensar"
print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente advinhar... ')
print('-=-' * 10)
jogador = int(input('Em que número eu pensei? ')) # Faz o jogado tentar advinhar
if jogador == computador :
    print("Parabens, você acertou ")
else:
    print('Eu pensei no número {} e não no número {}'.format(computador, jogador))
