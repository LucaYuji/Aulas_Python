# - ***Desafio 2  Condicionais***

# ***Você é um Dev Jr. e precisa criar um sistema de coletas de dados.*** 

# ***Utilize as condicionais, para escolher o tipo de dado e os métodos de lista*** 

# ***para:***

# - ***Mostra o dado;***
# - ***Alterar o dado;***
# - ***Coletando Dados de Experimentos***
# - ***Analisando a Soma de Dados ***
# - ***Localizar um Registro no Conjunto de Dados***

import random

aleatorio_1 = random.randint(4,11)
aleatorio_2 = random.randint((aleatorio_1 + 20), 131)
aleatorio_3 = random.randint(1,11)
criando_dados = list(range(aleatorio_1, aleatorio_2, aleatorio_3))
print('<<< Dados >>>')
print('')
print(criando_dados)
print('')
print('''Selecione uma Opção

0 - Alterar um Dado Especifico
1 - Coletar um Dado do Experimento
2 - Somatoria Dos Dados
3 - Localizando o Registro do Dado 
''')

escolhendo = int(input('>>>'))
print('')
if escolhendo == 0:
    posicao = criando_dados.index(int(input('Qual dado Deseja alterar? ')))
    criando_dados[posicao] = int(input('Selecione o novo valor desesejado >>> '))
    print('')
    print(criando_dados)
    print('')

elif escolhendo == 1:
    posicao2 = int(input('Qual a Posição do Dado que Deseja Coletar? '))
    dado_coleta_posicao = criando_dados[posicao2]
    print(f'Dado Obtido = {dado_coleta_posicao}')

elif escolhendo == 2:
    somatoria = sum(criando_dados)
    print(f'Somatoria dos Dados Obtidos = {somatoria}')
    print('')

elif escolhendo == 3:
    print(criando_dados)
    print('')
    localizando = criando_dados.index(int(input('Qual Dado deseja localizar? ')))
    print('')
    print(f'Local de Registro do dado = {localizando}')

else:
    print('Esta opção não existe !!!')