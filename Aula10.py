nome = str(input('Qual é o seu nome? '))
if nome ==  'Gustavo':
    print('Que nome lindo você tem!!')
    print('Bom dia {}'.format(nome))
else :
    print('Seu nome é tão normal!')
    print('Bom dia,{}'.format(nome))


    n1 = float (input('Digite a primeira nota: '))
    n2 = float (input('Digite a segunda nota: '))
    m = (n1 + n2)/2
    print ('A sua média foi {:.1f}'.format(m))
    if m >= 6.0:
        print('Sua média foi boa, parabéns!! ')
    else :
        print('Sua média não foi boa. Estude mais!!')

 
'''nome = str(input('Qual é o seu nome?'))
if nome == 'Leonardo': 
    print('Seu nome é lindo xará')
    print('Bom dia, {}!'.format(nome))
else : 
    print( '{}, seu nome é um nome comum'.format(nome))'''


