# Sem condicionais

# sistema de mercado onde eu consiga visualizar os produtos
# consiga escolher um produto
# import random
# n1 = random.randint(20,50)
# n2 = random.randint(20,50)
# n3 = random.randint(20,50)
# n4 = random.randint(20,50)

print('Produtos')
produtos = ['Arroz', 'Feijão', 'Carne', 'Refrigerante']
precos = [60.0, 70., 30., 20.]

# input de números inteiros referente ao indice da lista
# escolher1 = int(input('Produto 1 >>>'))
# escolher2 = int(input('Produto 2 >>>'))
# escolher3 = int(input('Produto 3 >>>'))
escolher1, escolher2, escolher3 = int(input('>>>')), int(input('>>>')), int(input('>>>'))
carrinho = []

# adicionando a escolha dentro da lista
# carrinho.append(escolher1)
# carrinho.append(escolher2)
# carrinho.append(escolher3)
# carrinho += (escolher1, escolher2, escolher3)
carrinho.extend(escolher1, escolher2, escolher3)

# criando uma lista e atribuindo na lista preços o indice de cada escolha
todos_os_valores = [precos[escolher1], precos[escolher2], precos[escolher3]]


# printando a lista e o resultado referente a conta anterior realizada
print(f'''
Produtos Selecionados
{produtos[escolher1], produtos[escolher2], produtos[escolher3]}
{todos_os_valores}
=========TOTAL=========
R$ {sum(todos_os_valores)}

''')

