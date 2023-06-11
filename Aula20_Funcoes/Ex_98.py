from time import sleep

def linha():
    print('-=' * 20)


def contador(i, f, p):
    print(linha)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1.0)

    if p < 0:
        p *= -1
    if p == 0:
        p = 1   
    if i < f: 
        cont = i 
        while cont <= f:
            print(f'{cont} ' , end ='', flush = True)
            sleep (0.5)
            cont += p 
        print('FIM!')
    else: 
        cont = i
        while cont >= f:
            print(f'{cont} ', end = '', flush = True )
            sleep(0.5)
            cont -= p
        print('FIM!')    

#Programa Principal 
contador(0, 100, 10)
contador(10, 0, 2)
print(linha)
print("Agora é a sua vez de personalizar a contagem!")
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)

