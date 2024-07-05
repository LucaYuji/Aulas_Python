import random


# Exercício 1: Coletando Dados de Experimentos
# Você está conduzindo experimentos em um laboratório para analisar o desempenho de diferentes modelos de machine learning.
# Utilize o método append() para adicionar os resultados de cada experimento à sua lista de resultados.
# resultados_experimentos = []


resultados_experimentos = []
aleatorio_1 = random.randint(0,101)
aleatorio_2 = random.randint(aleatorio_1,501)
aleatorio_3 = random.randint(1,11)
dados = list(range(aleatorio_1, aleatorio_2, aleatorio_3))
resultados_experimentos.append(dados)
print(resultados_experimentos)


# Exercício 2: Analisando a Soma de Dados de Vendas
# Você está trabalhando com dados de vendas de uma loja online. Utilize o
# método sum() para calcular o total de vendas realizadas durante um período
# de tempo específico.


precos = [150.00, 220.00, 180.00, 210.00, 190.00]
lista_valores_produtos = []

produto_1 = float(precos[0]) * (random.randint(0, 201))
produto_2 = float(precos[1]) * (random.randint(0, 201))
produto_3 = float(precos[2]) * (random.randint(0, 201))
produto_4 = float(precos[3]) * (random.randint(0, 201))
produto_5 = float(precos[4]) * (random.randint(0, 201))

lista_valores_produtos.extend([produto_1, produto_2, produto_3, produto_4, produto_5])

venda_diaria = sum(lista_valores_produtos)
vendas_por_hora = (venda_diaria / 24)
vendas_por_minuto = vendas_por_hora / 60
vendas_por_segundo = vendas_por_minuto / 60

print(f'''
--------------------------------------      
===== Relatório Diário de Vendas =====
--------------------------------------      
Venda Diária  >>>  {venda_diaria:.2f} R$
Vendas por Hora >>> {vendas_por_hora:.2f} R$
Vendas por Minuto >>> {vendas_por_minuto:.2f} R$
Vendas por Segundo >>> {vendas_por_segundo:.2f} R$
--------------------------------------
''')


# Exercício 3 : Identificando o Melhor Modelo de Machine Learning
# Você está comparando o desempenho de diferentes modelos de machine
# learning para um problema de classificação. Utilize o método max() para
# encontrar a precisão máxima alcançada pelos modelos.


precisoes = [0.85, 0.92, 0.78, 0.88, 0.90]
print('Maior Precisão',max(precisoes), sep= ' = ')


# Exercício 4: Limpeza de Dados
# Você recebeu um conjunto de dados para análise, mas ele está cheio
# de valores nulos e duplicados. Utilize o método clear() para limpar o
# conjunto de dados antes de começar a análise.


dados = [120, 130, None, 140, 120, 150, None]
dados.clear()
print(dados)


# Exercício 5: Copiando um Conjunto de Dados
# Você está trabalhando em um projeto de análise de dados em equipe e precisa
# compartilhar uma versão do conjunto de dados sem modificar o original.
# Utilize o método copy() para criar uma cópia do conjunto de dados.


dados_originais = [35, 40, 45, 50, 55]
dados_copia = dados_originais.copy()
print(dados_copia)


# Exercício 6 : Expandindo o Conjunto de Dados
# Durante a análise de dados, você percebe que precisa incluir mais amostras
# para obter resultados mais precisos. Utilize o método extend() para adicionar
# novas amostras ao conjunto de dados existente.


amostras = [0.5, 0.6, 0.7]
nova_amostra_1 = (random.randint(1,100)) / 10
nova_amostra_2 = (random.randint(1,100)) / 10
nova_amostra_3 = (random.randint(1,100)) / 10
nova_amostra_4 = (random.randint(1,100)) / 10
nova_amostra_5 = (random.randint(1,100)) / 10 
amostras.extend([nova_amostra_1, nova_amostra_2, nova_amostra_3, nova_amostra_4, nova_amostra_5])
print(amostras)


# Exercício 7: Contando Valores Únicos
# Você está explorando um conjunto de dados e deseja contar quantos valores
# únicos existem em uma determinada coluna. Utilize o método count() para contar
# a frequência de cada valor na coluna.


coluna = ["A", "B", "C", "A", "B", "D", "E"]
quant = coluna.count("B")
print(quant)


# Exercício 8: Localizando um Registro no Conjunto de Dados
# Durante a análise de dados, você precisa encontrar a posição de um
# registro específico no conjunto de dados. Utilize o método index() para localizar
# o registro desejado.


registros = ["ID-001", "ID-002", "ID-003", "ID-004"]
print(registros.index('ID-002'))


# Exercício 9 : Inserindo Novos Dados no Conjunto
# Durante a análise de dados, você recebe novos registros que
# precisam ser adicionados ao conjunto de dados existente.
# Utilize o método insert() para inserir os novos registros na posição desejada.


registros = ["ID-001", "ID-002", "ID-004", "ID-005"]
registros.insert(0,'ID-000')
print(registros)
