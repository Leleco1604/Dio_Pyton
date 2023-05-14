#Faça um programa que leia 3 número e diga qual é o maior e o menor entre eles

a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
#verificando quem é o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = a
if c>a and c>b:
    maior = c

print('O menor valor digitado é: {}'.format(menor))
print('O maior valor digitado é: {}'.format(maior))