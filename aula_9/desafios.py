import numpy as np
# Desafio 1:
# 1. Crie um array de 20 elementos.
# 2. Extraia os primeiros 5 elementos, os últimos 5 
# elementos e os elementos 
# das posições 5 a 10.


def extrair():
    array1 = np.arange(1,21)
    primeiros = array1[0:5]
    utltimos = array1[-5:]
    elementos = array1[5:10]
    print('Array Completa ->',array1)
    print('5 primeiros elementos ->',primeiros)
    print('5 últimos elementos ->',utltimos)
    print('5 até 10 ->',elementos)
extrair()


# Desafio 2:
# 1. Crie duas matrizes 3x3.
# 2. Calcule o produto.


def produto(matriz1, matriz2):
    produto = matriz1 @ matriz2
    return produto
def matriz():
    matriz1 = np.random.randint(0,10,(3,3)) 
    matriz2 = np.random.randint(0,10,(3,3))
    return matriz1, matriz2
def main():
    matriz1, matriz2 = matriz()
    cal = produto(matriz1, matriz2)
    print(f'''
Matriz 1
------------          
{matriz1}  
------------

Matriz 2
------------
{matriz2}
------------

O produto das Matrizes 
------------
{cal}
------------
''')
main()


# Desafio 3:
# Criação de Arrays:
# Crie um array de 1 a 10.
# Crie uma matriz 3x3 com valores aleatórios entre 0 e 1.



def matriz11():
    matriz3 = np.arange(1,11)
    matriz4 = np.random.randint(0,10,(3,3))
    print(matriz3,'\n-------------','\n', matriz4)
    return matriz3, matriz4
matriz11()


# Operações Básicas:
# Desafio 4:
# Calcule a soma dos elementos do array.
# Encontre o valor máximo e mínimo do array.


def matriz111():
    matriz5 = np.random.randint(0,10,(3,3)) 
    matriz6 = np.random.randint(0,10,(3,3))
    return matriz5, matriz6

def soma(matriz5, matriz6):
    soma = matriz5 + matriz6
    return soma

def coleta(matriz5, matriz6):
    concatenar = np.concatenate([matriz5, matriz6])
    maximo = np.max(concatenar)    
    minimo = np.min(concatenar)
    return maximo, minimo
def display(somando, maximo, minimo):
    print(f'''
Somatoria das matrizes 
----------------------
{somando}          
----------------------

Valor Máximo entre matrizes -> {maximo}
Valor Mínimo entre matrizes -> {minimo}
''')

def main1():
    matriz5, matriz6 = matriz111()
    somando = soma(matriz5, matriz6)
    maximo, minimo = coleta(matriz5, matriz6)
    display(somando, maximo, minimo)
main1()


# Funções Estatísticas:
# Desafio 5:
# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.


def matriz1111():
    matriz7 = np.random.randint(0,10,(3,3)) 
    matriz8 = np.random.randint(0,10,(3,3))
    return matriz7, matriz8
def media_mediana(matriz7, matriz8):
    cal2 = matriz7.T @ matriz8.T
    media = np.mean(cal2)
    mediana = np.median(cal2)
    print(f'''
Produto das Matrizes Transpostas
--------------------
{cal2}    

Média do Produto -> {media:.2f}
Mediana do Produto -> {mediana:.2f}
''')
    
def main11():
    matriz7, matriz8 = matriz1111()
    media_mediana(matriz7, matriz8)
# main11()


# Manipulação de Arrays:
# Desafio 6:
# Adicione 10 a todos os elementos do array.
# Reshape o array 1D para um array 2D (2x5).


def adicionar():
    lista = [] 
    for x in list(range(1,11)):
        lista.append(10)
    return lista

def reshape1():
    lista = adicionar()
    array = np.array(lista)
    array_new = array.reshape(2,5)
    print(array_new)
reshape1()