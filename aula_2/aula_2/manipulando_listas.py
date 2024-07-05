lista = [1,2,6,6,9,5,1278,56,0]
lista2 = ['a','b','c']
lista3 = [1.,2.,3.]
lista4 = [True, False, True, True]

valor = lista[0]  # atribuindo a uma variável um indice do vetor
lista[0] = 10  # atribuindo valor para o vetor
soma = sum(lista4)
print(soma)
print(lista)

# count a quantidade de um determinado valor
contar = lista.count(6)
print(contar)

# len mostra o comprimento da lista, quantos indíces tem na lista
comprimento = len(lista)
print(comprimento)

# organizar a lista
organizado = sorted(lista)
print(organizado)
lista.sort(reverse = True)
print(lista)

#min menor número
#mac maio número
menor = min(lista)
maior = max(lista)
print(maior, menor, sep=' > ')

#copiando a lista
lista7 = lista.copy()
print(lista7)

# juntando as listas
lista8 = lista7 + lista2
print(lista8)

#exclui o último item da lista
lista2.pop()
print(lista2)

#exclui um indice em especifico
lista2.remove('a')
print(lista2)

#excluindo um valor numerado pelo indice
del lista2[0]
print(lista2)

# insere uma posição(indíce) e o valor
lista2.insert(0,'z')
print(lista2)

numero = int(input('>>'))
valor = input('>>')
lista2.insert(numero, valor)
print(lista2)

b1 = 10
b2 = 20
b3 = 40 
lista2.extend([b1,b2,b3])
lista += (b1,b2,b3)
print(lista2, lista)

# append adicionar por dado

lista2.append(10)
lista2.append(20)


# qual lista está este objeto
indice = lista2.index('z')
print(indice)