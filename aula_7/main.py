## ***Desafio 2***

# ***VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA.*** 

# ***SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE COM ESTATISTICA A MODA ,  MEDIA, MEDIANA E DESVIO DE PADRÃO, DAS NOTAS DE ALUNOS DE UM COLÉGIO, ALÉM DE MOSTRAR  A MENOR E A  MAIOR NOTA, SEPARE EM FUNÇÕES DIFERENTES, CRIE MÓDULOS.***  

# ***1 -  VOCÊ CRIAR SEUS PRÓPRIOS MÓDULOS***

# ***2 - OU USAR STATISTICS(com módulos)*** 

# ***3 - Utilize Parâmetros, caso deixe mais flexível***

import numpy as np
import statistics
from function import *
import os


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
main()


