from bs4 import BeautifulSoup
import requests
import pandas as pd
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Qual região compra mais produtos? 

def vendedores():
    # Coleta de dados
    url = 'https://bea3853.github.io/site_teste/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dados = soup.find('table')

    vendedor = []
    q_compras = []
    regiao = []

    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        vendedor.append(n[0].text)
        q_compras.append(int(n[1].text))
        regiao.append(n[2].text)

    # Limpeza de dados
    #busca automatica de nomes e vincular com a compra e região
    concatenar = zip(vendedor,q_compras,regiao) # agupa valores da lista com mesmo índice
    df = pd.DataFrame(concatenar)
    # print(df)

    local_joao = []
    local_maria = []
    local_pedro = []
    local_ana = []
    lista_molde = vendedor
    lista_nomes = []
    n = 0
    while n != len(vendedor):
        nomes = vendedor[n]
        for nomes in vendedor:
            match nomes:
                case 'João':
                    local_joao.append(lista_molde.index('João'))
                    lista_molde.remove('João')
                    lista_molde.insert(n,0)
                    lista_nomes.append('João')
                    n += 1
                case 'Maria':
                    local_maria.append(lista_molde.index('Maria'))
                    lista_molde.remove('Maria')
                    lista_molde.insert(n,0)
                    lista_nomes.append('Maria')
                    n += 1
                case 'Pedro':
                    local_pedro.append(lista_molde.index('Pedro'))
                    lista_molde.remove('Pedro')
                    lista_molde.insert(n,0)
                    lista_nomes.append('Pedro')
                    n += 1
                case 'Ana':
                    local_ana.append(lista_molde.index('Ana'))
                    lista_molde.remove('Ana')
                    lista_molde.insert(n,0)
                    lista_nomes.append('Ana')
                    n += 1

    lista_nomes_limpa = list(sorted(set(lista_nomes)))
    # vendas por vendedor
    soma_vendas_joao = sum(df.iloc[local_joao,1])
    soma_vendas_maria = sum(df.iloc[local_maria,1])
    soma_vendas_pedro = sum(df.iloc[local_pedro,1])
    soma_vendas_ana = sum(df.iloc[local_ana,1])
    lista_vendas = [soma_vendas_ana, soma_vendas_joao,soma_vendas_maria,soma_vendas_pedro]

    # Criar a figura
    fig, grafico = plt.subplots()
    grafico.pie(lista_vendas, labels=lista_nomes_limpa, autopct='%.1f%%')
    grafico.set_title('Vendas por Vendedor')

    # mostrar o grafico
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def regioes():
    url = 'https://bea3853.github.io/site_teste/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dados = soup.find('table')

    vendedor = []
    q_compras = []
    regiao = []

    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        vendedor.append(n[0].text)
        q_compras.append(int(n[1].text))
        regiao.append(n[2].text)

    # Limpeza de dados
    #busca automatica de nomes e vincular com a compra e região
    concatenar = zip(vendedor,q_compras,regiao) # agupa valores da lista com mesmo índice
    df = pd.DataFrame(concatenar)
    # print(df)

    # vendas por região
        
    local_sul = []
    local_sudeste = []
    local_centro_oeste = []
    local_nordeste = []
    local_norte = []
    lista_molde_regiao = regiao
    lista_regioes = []
    x = 0
    while x != len(regiao):
        local = regiao[x]
        for local in regiao:
            match local:
                case 'Sul':
                    local_sul.append(lista_molde_regiao.index('Sul'))
                    lista_molde_regiao.remove('Sul')
                    lista_molde_regiao.insert(x,0)
                    lista_regioes.append('Sul')
                    x += 1
                case 'Sudeste':
                    local_sudeste.append(lista_molde_regiao.index('Sudeste'))
                    lista_molde_regiao.remove('Sudeste')
                    lista_molde_regiao.insert(x,0)
                    lista_regioes.append('Sudeste')
                    x += 1
                case 'Centro-Oeste':
                    local_centro_oeste.append(lista_molde_regiao.index('Centro-Oeste'))
                    lista_molde_regiao.remove('Centro-Oeste')
                    lista_molde_regiao.insert(x,0)
                    lista_regioes.append('Centro-Oeste')
                    x += 1
                case 'Nordeste':
                    local_nordeste.append(lista_molde_regiao.index('Nordeste'))
                    lista_molde_regiao.remove('Nordeste')
                    lista_molde_regiao.insert(x,0)
                    lista_regioes.append('Nordeste')
                    x += 1
                case 'Norte':
                    local_norte.append(lista_molde_regiao.index('Norte'))
                    lista_molde_regiao.remove('Norte')
                    lista_molde_regiao.insert(x,0)
                    lista_regioes.append('Norte')
                    x += 1
    
    lista_regioes_limpa = list(sorted(set(lista_regioes)))

    soma_vendas_sul = sum(df.iloc[local_sul,1])
    soma_vendas_sudeste = sum(df.iloc[local_sudeste,1])
    soma_vendas_centro_oeste = sum(df.iloc[local_centro_oeste,1])
    soma_vendas_nordeste = sum(df.iloc[local_nordeste,1])
    soma_vendas_norte = sum(df.iloc[local_norte,1])

    lista_regioes_vendas = [soma_vendas_centro_oeste, soma_vendas_nordeste, soma_vendas_norte, soma_vendas_sudeste, soma_vendas_sul]

    fig, grafico = plt.subplots()
    grafico.bar(lista_regioes_limpa, lista_regioes_vendas, color='green')
    grafico.set_title('Vendas por Região')
    grafico.set_xlabel('Regiões')
    grafico.set_ylabel('Qant. Vendas')  
    plt.grid(True)
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH)


def produtos():
    url = 'https://bea3853.github.io/site_teste/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    dados = soup.find('table')

    vendedor = []
    q_compras = []
    regiao = []

    linhas = dados.find_all('tr')[1:]
    for linha in linhas:
        n = linha.find_all('td')
        vendedor.append(n[0].text)
        q_compras.append(int(n[1].text))
        regiao.append(n[2].text)

    # Limpeza de dados
    #busca automatica de nomes e vincular com a compra e região
    concatenar = zip(vendedor,q_compras,regiao) # agupa valores da lista com mesmo índice
    df = pd.DataFrame(concatenar)
    # print(df)    
    estatistica = df.describe()
    total_vendas = estatistica.iloc[0,0]
    media = estatistica.iloc[1,0]
    desvio_padrao = estatistica.iloc[2,0]
    menor_venda = estatistica.iloc[3,0]
    maior_venda = estatistica.iloc[7,0]
    text.config(text=f'''
Total de Pedidos -> {total_vendas:.2f}
Media de Vendas -> {media:.2f}
Desvio Padrão das Vendas -> {desvio_padrao:.2f}
Maior Venda -> {maior_venda:.2f}
Menor Venda -> {menor_venda:.2f}
''')

# janela tkinter
janela = tk.Tk()
janela.title('Gráfico de Vendas')

# button
btn = tk.Button(janela, text='Gráfico Vendedores', command=vendedores)
btn.pack(pady=20)

btn = tk.Button(janela, text='Gráfico Regiões', command=regioes)
btn.pack(pady=20)

text = tk.Label(janela, text='Estatistica', fg='white', bg='black')
text.pack(pady=5)
btn2 = tk.Button(janela, text='Relátorio',command=produtos)
btn2.pack(pady=5)

# loop tkinter
janela.mainloop()
#index() retorna o primeiro indice do item encontrado na lista
#count() conta a quantidade de ocorrências de um elemento na lista
# print(vendedor,q_compras,regiao)