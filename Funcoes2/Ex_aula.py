""" def contador (i,f,p):
    c = i
    while c <= f:
        print(f'{c} ', end= '')
        c += p
        print('FIM!') """

""" 
contador(2,10,2) 

 def contador (i,f,p):...

help(contador) """ 

# Exemplo de Escopo 
""" 
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


'''Programa Principal'''    

n = 2
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')

teste() """

# Retorno de Valores  
""" 
def somar(a=0,b=0,c=0):
    s = a+b+c
    return s


r1 = somar (3,2,5) 
r2 = somar (1,7)
r3 = somar (4)
print(f'Meus calculos deram {r1}, {r2} e {r3}') """

