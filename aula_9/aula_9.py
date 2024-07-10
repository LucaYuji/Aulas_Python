import numpy as np
import matplotlib.pyplot as plt
import timeit

# vetor = [1,2,3,4,4]
# array = np.array([[vetor],[vetor]])
# print(array + array @ array)

# # cria uma matriz
# vetor = np.array([[2,3],[5,4]])
# print(vetor)
# vetor = vetor.T
# print(vetor)
# # cria uma lista
# vetor2 = np.arange(1,20)
# print(vetor2)

# # números aleatórios
# vetor3 = np.random.randint(1,21)
# print(vetor3)

# # vetor uns

# vetor5 = np.ones(20)
# print(vetor5)

# # vetor zeros
# vetor6 = np.zeros(10)
# print(vetor6)

# #espaçamento padrão
# # a cada 10 
# vetor7 = np.linspace(1,10)
# print(vetor7)


# # vetor tem uma linha so


# # calculos matematicos
# maior = np.max(vetor2)
# menor = np.min(vetor2)
# raiz = np.sqrt(vetor2)
# media = np.mean(vetor2)
# mediana = np.median(vetor2)
# desvio = np.std(vetor2)
# print(maior,menor,raiz,media,mediana,desvio)


# matriz = np.array([[1,2,3], [14,5,6],[7,8,9]])
# print(matriz)

# # acessar a matriz
# acessar = matriz[0][1] linha, coluna
# acessar2 = matriz[0,1] # linha,coluna
# matriz[0,1] = 20
# print(acessar, acessar2)
# print(matriz)
# def ola():
#     ola1 = matriz @ matriz.T
#     print(ola1)
# ola()

# matriz1 = np.array([[1,2,3],[14,5,6],[7,8,9]])
# percorrer = matriz1[1:2] # percorrendo de tal linha ate o final

vetor = np.arange(1,30)
percorrer = vetor[4:10]
print(percorrer)
# print(percorrer)

# matriz2 = np.array([[1,2,3],[14,5,6],[7,8,9]])
# matriz3 = np.array([[1,2,3],[14,5,6],[7,8,9]])
# calculo = (matriz1 @ matriz2.T) + matriz3

# concatenar_matriz = np.concatenate([matriz2,matriz3])
# print(concatenar_matriz)
# print(calculo)

# forma = np.shape(matriz1) # contagem da matriz
# print(forma)

# forma = np.info(matriz1) # traz todas as informações da array
# print(forma)

# forma = np.ndim(matriz1) # dimensão da matriz
# print(forma)

# x = np.array([1,11])
# y = np.array([1,11])

# def soma1():
#     lista = list(range(1, 2000))
#     return lista

# soma1()
# def soma2():
#     aleatorio1 = np.random.randint(1,10,(5,10))
#     soma2 = np.sum(aleatorio1)
#     return soma2
# # print(soma2)
# soma2()
# time1 = timeit.timeit(soma1, number=10)
# print(time1)
# time = timeit.timeit(soma2, number=10)
# print(time)


# aleatorio2 = np.random.randint(1,20,(10,5))
# plt.scatter(aleatorio1,aleatorio2)
# plt.show()

# plt.pie(x, labels=y, )
# aleatorio = np.random.randint(1,10,(10,5)) # (start,stop(colunas)) ou (start,stop(linhas, colunas, quantidade de matriz))
# indice = aleatorio[2, 4] #[linha, coluna]
# print(indice)
# print(aleatorio)
