import numpy as np
import statistics
import matplotlib.pyplot as plt


def valores(lista, nome_lista):
    print('')
    print('Digite as notas')
    nome = input('Nome do Aluno(a) -> ')
    for x in [0,1,2,3]:
        x += 1
        n = float(input(f'{x}º Bimestre -> Nota = '))
        lista.append(n)
    print('')
    print('')
    nome_lista.append(nome)

def media_aluno(lista, lista_media_por_aluno):
    media_por_aluno = np.mean(lista)
    lista_media_por_aluno.append(media_por_aluno)


def media(lista_media_por_aluno):
    media_total = np.mean(lista_media_por_aluno)
    return media_total


def mediana(lista_media_por_aluno):
    mediana_total = np.median(lista_media_por_aluno)
    return mediana_total


def moda(lista_media_por_aluno):
    moda_total = statistics.mode(lista_media_por_aluno)
    return moda_total


def desvio_padrao(lista_media_por_aluno):
    desvio_padrao_total = np.std(lista_media_por_aluno)
    return desvio_padrao_total


def visor(media_total, mediana_total, moda_total, desvio_padrao_total, turma, materia, nome_lista, lista_media_por_aluno):
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

Alunos(as) da Turma {turma}
{nome_lista}

''')

def grafics(lista_media_por_aluno, nome_lista):
    plt.bar(nome_lista, lista_media_por_aluno, edgecolor='black', color='green')
    plt.plot(nome_lista, lista_media_por_aluno, marker='o', color='black')
    plt.xlabel('Alunos')
    plt.ylabel('Média')
    plt.title('Histograma')
    plt.grid(True)
    plt.show()


