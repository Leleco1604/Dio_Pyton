""" Faça um programa que tenha uma função notas© qua poda recabar
várias notas de alunos a vai retornar um dicionário com as seguintas informaçãos:
- Quantidada de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
"""

def notas(*n, sit = False ):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)
    if sit:
        if r['média'] >= 7:
           r['situação'] = 'Parabens,você foi aprovado'
        elif r['média'] >= 5:
            r['situação'] = 'Você vai para final...'
        else:
            r['situação'] = 'Você está reprovado'
        
    return r 


#Programa Principal
resp = notas(5.5,2.5,8.5, sit = True)
print(resp) 