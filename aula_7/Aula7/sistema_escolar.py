import numpy as np
import statistics

# auto py to exe

def valores(lista):
    print('')
    print('Digite as notas')
    for x in [0,1,2,3]:
        x += 1
        n = float(input(f'{x}º Bimestre -> Nota = '))
        lista.append(n)
    print('')
    print('')


def media_aluno(lista, lista_media_por_aluno):
    media_por_aluno = np.mean(lista)
    lista_media_por_aluno.append(media_por_aluno)


def media(lista_media_por_aluno):
    media_total = np.mean(lista_media_por_aluno)
    return media_total


def mediana(lista_media_por_aluno):
    lista_media_por_aluno.sort()
    mediana_total = np.median(lista_media_por_aluno)
    return mediana_total


def moda(lista_media_por_aluno):
    moda_total = statistics.mode(lista_media_por_aluno)
    return moda_total


def desvio_padrao(lista_media_por_aluno):
    desvio_padrao_total = np.std(lista_media_por_aluno)
    return desvio_padrao_total


def visor(media_total, mediana_total, moda_total, desvio_padrao_total, turma, materia):
    print(f'''
--------------------------------------          
    Designação da Turma -> {turma}
           Matéria -> {materia}
--------------------------------------
          Dados da Turma
--------------------------------------
Média           ->      {media_total:.2f}
Mediana         ->      {mediana_total:.2f}
Moda            ->      {moda_total:.2f}
Desvio Padrão   ->      {desvio_padrao_total:.4f} 
--------------------------------------
''')

def main():
    lista_media_por_aluno = []
    lista = []
    condicao = 1
    materia = input('Matéria: ')
    turma = input('Designação da Turma: ')
    while condicao != 0:  
        valores(lista)
        media_aluno(lista, lista_media_por_aluno)
        condicao = int(input('Deseja Adiciona um Novo Aluno? s=1 / n=0 -> '))
    media_total = media(lista_media_por_aluno)
    mediana_total = mediana(lista_media_por_aluno)
    moda_total = moda(lista_media_por_aluno)
    desvio_padrao_total = desvio_padrao(lista_media_por_aluno)
    visor(media_total, mediana_total, moda_total, desvio_padrao_total, turma, materia)
    ola = input('Aperte qualque tecla para sair ...')
main()