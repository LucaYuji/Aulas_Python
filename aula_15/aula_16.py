import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import tkinter as tk
import numpy as np

# Quais os generos musicais mais populares

def popular():
    dados = pd.read_csv('aula_15\spotify_tracks.csv')
    genero = dados['genre'].to_list()
    popularidade = dados['popularity'].to_list()
    lista_dados = list(zip(genero,popularidade))
    df = pd.DataFrame(lista_dados)
            
    local_acustic = []
    local_afrobeat = []
    local_altrock = []
    local_alternative = []
    local_ambient = []
    lista_molde_genero = genero
    lista_genero = []
    x = 0
    while x != len(genero):
        local = genero[x]
        for local in genero:
            match local:
                case 'acustic':
                    local_acustic.append(lista_molde_genero.index('acustic'))
                    lista_molde_genero.remove('acustic')
                    lista_molde_genero.insert(x,0)
                    lista_genero.append('Acustic')
                    x += 1
                case 'afrobeat':
                    local_afrobeat.append(lista_molde_genero.index('afrobeat'))
                    lista_molde_genero.remove('afrobeat')
                    lista_molde_genero.insert(x,0)
                    lista_genero.append('Afrobeat')
                    x += 1
                case 'alt-rock':
                    local_altrock.append(lista_molde_genero.index('alt-rock'))
                    lista_molde_genero.remove('alt-rock')
                    lista_molde_genero.insert(x,0)
                    lista_genero.append('Alt-Rock')
                    x += 1
                case 'alternative':
                    local_alternative.append(lista_molde_genero.index('alternative'))
                    lista_molde_genero.remove('alternative')
                    lista_molde_genero.insert(x,0)
                    lista_genero.append('Alternative')
                    x += 1
                case 'ambient':
                    local_ambient.append(lista_molde_genero.index('ambient'))
                    lista_molde_genero.remove('ambient')
                    lista_molde_genero.insert(x,0)
                    lista_genero.append('Ambiente')
                    x += 1

    lista_genero_limpa = list(sorted(set(lista_genero)))

    soma_popularidade_acustic = sum(df.iloc[local_sul,1])
    soma_popularidade_afrobeat = sum(df.iloc[local_sudeste,1])
    soma_popularidade_altrock = sum(df.iloc[local_centro_oeste,1])
    soma_popularidade_alternative = sum(df.iloc[local_nordeste,1])
    soma_popularidade_ambient = sum(df.iloc[local_norte,1])

    lista_genero_popularidade = [soma_vendas_centro_oeste, soma_vendas_nordeste, soma_vendas_norte, soma_vendas_sudeste, soma_vendas_sul]

    fig, grafico = plt.subplots()
    grafico.bar(lista_genero_limpa, lista_genero_popularidade, color='green')
    grafico.plot(lista_genero_limpa, lista_genero_popularidade)
    grafico.set_title('Popularidade por Gênero Musical')
    grafico.set_xlabel('Gênero Musical')
    grafico.set_ylabel('Popularidade')  
    plt.grid(True)
    canvas = FigureCanvasTkAgg(fig, master = janela)
    canvas.draw()
    canvas.get_tk_widget().pack(side = tk.RIGHT, fill=tk.BOTH)

janela = tk.Tk()
janela.title('Popularidade Musical')
btn = tk.Button(janela, text='Gráfico Popularidade Musical', command=popular)
btn.pack(pady=20)
janela.mainloop()



























# local_joao = []
# local_maria = []
# local_pedro = []
# local_ana = []
# lista_molde = vendedor
# lista_nomes = []
# n = 0
# while n != len(vendedor):
#     nomes = vendedor[n]
#     for nomes in vendedor:
#         match nomes:
#             case 'João':
#                 local_joao.append(lista_molde.index('João'))
#                 lista_molde.remove('João')
#                 lista_molde.insert(n,0)
#                 lista_nomes.append('João')
#                 n += 1
#             case 'Maria':
#                 local_maria.append(lista_molde.index('Maria'))
#                 lista_molde.remove('Maria')
#                 lista_molde.insert(n,0)
#                 lista_nomes.append('Maria')
#                 n += 1
#             case 'Pedro':
#                 local_pedro.append(lista_molde.index('Pedro'))
#                 lista_molde.remove('Pedro')
#                 lista_molde.insert(n,0)
#                 lista_nomes.append('Pedro')
#                 n += 1
#             case 'Ana':
#                 local_ana.append(lista_molde.index('Ana'))
#                 lista_molde.remove('Ana')
#                 lista_molde.insert(n,0)
#                 lista_nomes.append('Ana')
#                 n += 1

# lista_nomes_limpa = list(sorted(set(lista_nomes)))
# # vendas por vendedor
# soma_vendas_joao = sum(df.iloc[local_joao,1])
# soma_vendas_maria = sum(df.iloc[local_maria,1])
# soma_vendas_pedro = sum(df.iloc[local_pedro,1])
# soma_vendas_ana = sum(df.iloc[local_ana,1])
# lista_vendas = [soma_vendas_ana, soma_vendas_joao,soma_vendas_maria,soma_vendas_pedro]

# # Criar a figura
# fig, grafico = plt.subplots()
# grafico.pie(lista_vendas, labels=lista_nomes_limpa, autopct='%.1f%%')
# grafico.set_title('Vendas por Vendedor')

# # mostrar o grafico
# canvas = FigureCanvasTkAgg(fig, master=janela)
# canvas.draw()
# canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

