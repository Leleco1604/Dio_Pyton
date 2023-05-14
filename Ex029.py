velocidade = float(input('Qual pe a velocidade do carro?'))
if velocidade >= 80:
     print('MULTADO! você excedeu o limite permitido que é de 80km/h')
     multa = (velocidade - 80) * 7
     print('Você deve pagar um multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia, diriga com segurança')
