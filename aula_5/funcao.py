# semântica, dar o nome daquilo que faz.
# verbo para definir o nome. preferncial em inglês
# indentação (espaços)
# objetivo da função é encapsular scripts
# crio um escopo para a minhas instruções

# def calculadora():
#     n1 = float(input('>>>'))

#     def soma(n1):
#         resultado = 10 + n1
#         return resultado

#     def sub(n1):
#         resultado = 10 - n1
#         return resultado

#     def mult(n1):
#         resultado = 10 * n1
#         return resultado

#     def div(n1):
#         resultado = 10 / n1
#         return resultado

#     print(f'{soma(n1):,.2f} | {sub(n1):,.2f} | {mult(n1):,.2f} | {div(n1):,.2f}')

# calculadora()




# calculadora com funções

# def soma(n1, n2):
#     return n1 + n2

# def sub(n1, n2):
#     return n1 - n2

# def mult(n1, n2):
#     return n1 * n2

# def div(n1, n2):
#     return n1 / n2

# def calculadora():
#     n = 1
#     while n != 0:
#         n1 = float(input('>>>'))
#         operacao = input('+ , - , * , /   ')
#         n2 = float (input('>>>'))
#         if operacao == '+':
#             print('Resultado = ', soma(n1,n2))
#             n = int(input('continuar? não = 0'))
#         elif operacao == '-':
#             print('Resultado = ', sub(n1,n2))
#             n = int(input('continuar? não = 0'))
#         elif operacao == '*':
#             print('Resultado = ', mult(n1,n2))
#             n = int(input('continuar? não = 0'))
#         elif operacao == '/':
#             print('Resultado = ', div(n1,n2))
#             n = int(input('continuar? não = 0'))
#         else:
#             print('Esta operação NÃO existe')
#             n = int(input('continuar? não = 0'))

# calculadora()




def form(nome, email, lista, lista_total):
    print('SEJA BEM VINDO(A)', nome)
    print('SEJA BEM VINDO(A)', email)
    print('Acesse o tipo de produto: ')
    carrinho_de_compras = []
    total = []
    deseja_fazer_pedido = input('Deseja fazer um pedido? Digite S / s ')
    while deseja_fazer_pedido == 's' or deseja_fazer_pedido == 'S':
        escolha = int(input('''

                    0 - eletronicos
                    1 - cama mesa e banho
                    2 - games
                    3 - livros

                            '''))
        
        carrinho_de_compras.append(lista[escolha])
        total.append(lista_total[escolha])
        deseja_fazer_pedido = input('Deseja fazer um pedido? Digite S / s ')
        soma = sum(total)
        print(carrinho_de_compras)
        print(f'valor total = R$ {soma:,.2f}')
        
    else:
        print('suas compras', carrinho_de_compras)
        return carrinho_de_compras

def forma_de_pagamento(valores, escolha_pag):
    print('FOMRAS DE PAGAMENTO >>> 1 PIX | 2 CC | 3 PAYPALL')
    if escolha_pag == '1' or '2' or '3':
        total = sum(valores_lista)
        print('Obrigado até logo')

def main():
    lista = ['eletronicos', 'cama, mesa e banho', 'games', 'livros']
    valores_lista = [150.78, 50.89, 150.90, 56.99]
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    form(nome, email, lista, valores_lista)


main()    