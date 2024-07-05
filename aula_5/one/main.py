from defs import*

def main():
    n = 1
    lista = []
    name = input('Nome do Aluno: ')
    materia = input('Matéria: ')
    valores(n,lista)
    cal = calculo(lista)
    apr = aprovacao(cal)
    visor(lista, cal, apr, name, materia)
main()