#Aumente o salário de um funcionario em 15% ou em 10%

salario = float(input('Qual é o seu salário? R$'))
if salario <= 1250.00:
    print('Seu novo salário é: {}'.format((salario * 0.15)+ salario))
else:
    print('Seu novo salário é: {}'.format((salario * 0.1) + salario))