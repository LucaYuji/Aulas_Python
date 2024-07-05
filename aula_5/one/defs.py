# 1 - Com funções crie um sistema de médias.
def valores(n,lista):
    print('')
    print('Digite as notas')
    while n != -1:
        n = float(input('>>>'))
        lista.append(n)
    lista.pop()
    print('')
    print('')

def calculo(lista):
    calculo = (sum(lista) / len(lista))
    return calculo

def aprovacao(cal):
    if cal >= 6:
        apr = 'Aprovado'
    elif cal < 6:
        apr = 'Reprovado'
    return apr

def visor(lista, cal, apr, name, materia):
    print('------------------')
    for x in list(range(0,(len(lista)))):
        print(f'{int(x + 1)}º Nota = {(lista[x]):.1f}')
    print('------------------')
    print(f'''
------------------------
Aluno = {name}
Matéria = {materia}
Maior Nota = {max(lista):.1f}
Menor Nota = {min(lista):.1f}
Média = {cal:.1f}
Status = {apr}
------------------------
        ''') 
    
        

