# # condicionais em python
# # condicional simples
# if 2 < 1:
#     print('É maior')


# nome = input('Digite seu nome ')

# # Se existir faça isso
# if nome:
#     print('Seja bem vindo', nome)

# if nome == 'José':
#     print('Seja bem vindo', nome)

# if 'a' in nome:
#     print('existe a letra a no nome')

# lista = [1,6,6,6,6]

# tupla = (5,5,6,3)

# if 6 in lista and 10 in tupla:
#     print('Existe')

# if nome != 'Carol':
#     print('Não')


# senha = 1234
# login = 'fdsa'
# senha_usuario = input('Digite a senha ')
# login_usuario = input('Digite o login ')

# if senha == senha_usuario and login == login_usuario: 
#     print('Acesso liberado')
    
# elif senha == senha_usuario or login == login_usuario:
#     print('Você digitou algo incorreto')
# else:

#     print('Tente novamente')


n1 = float(input('>>>'))
n2 = float(input('>>>'))
# print('+  |  -  |  *  |  /')
operacao = input('operação')
if operacao == '+':
    soma = n1 + n2
    print(soma)
elif operacao == '-':
    sub = n1 - n2
    print(sub)
elif operacao == '*':
    mult = n1 * n2
    print(mult)
elif operacao == '/':
    n2 = float(input('>>>'))
    div = n1 / n2
    print(div)