# Crie um sistema de banco, com as seguintes operações:

# # SISTEMA DE BANCO 

# - Acesso a conta
# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema

# Gerando um valor para conta
import time
import random
valor_da_conta = float(random.randint(100000, 500000))

# Cadastro
print('')
print('CADASTRO DA CONTA')
print('')

# Adicionando valores para comparação
nome = []
senha = []
nome3, senha3, email = input('Nome Completo: '), int(input('Senha: ')), input('E-mail: ')
nome.append(nome3)
senha.append(senha3)

# Adicionando valores a lista
nome_conta = []
senha_conta = []

# Acessando a Conta
n = 0
confirmar = []
while n != 3:
    print('')
    print('<<< ACESSO A CONTA >>>')
    print('')
    nome1 = input('Nome Completo: ')
    senha1 = int(input('Senha: '))
    nome_conta.append(nome1)
    senha_conta.append(senha1)
    if nome_conta == nome and senha_conta == senha:
        n = 3
        confirmar.clear()
        confirmar1 = True
        confirmar.append(confirmar1)
    else:
        print('')
        print('Alguma informação está ERRADA')
        print('')
        # Limpando a lista para novos
        nome_conta.clear()
        senha_conta.clear()
        n += 1
        confirmar.clear()
        confirmar2 = False
        confirmar.append(confirmar2)



if confirmar == [True]:
    x = 1
    while x != 0:

        escolhendo = int(input('''
Escolha uma das opções abaixo:
---------------------------------
        0 - Ver Extrato
        1 - Deposito
        2 - Saque
        3 - Finalizar
---------------------------------
>>>
        '''))
        if escolhendo == 0:
            print(f'Seu Saldo Altual é: R$ {valor_da_conta:.2f}')
            x = int(input('Deseja realizar uma nova operação? sim = 1 | não = 0'))
        elif escolhendo == 1:
            deposito = float(input('Valor do depósito (R$): '))
            saldo_atual = valor_da_conta + deposito
            x = int(input('Deseja realizar uma nova operação? sim = 1 | não = 0'))
        elif escolhendo == 2:
            saque = float(input('Valor o Saque (R$): '))
            saldo_atual = valor_da_conta - saque
            x = int(input('Deseja realizar uma nova operação? sim = 1 | não = 0'))
        elif escolhendo == 3:
            x = int(input('Tem certeza que deseja encerrar a operação? sim = 1 | não = 0'))
        else:
            print('Está opção não existe, SELECIONE uma opção VÁLIDA')
            time.sleep(2)
    else:
        print('Operação Finalizado, Volte Sempre')


elif confirmar == [False]:
    print('SUA CONTA FOI BLOQUEADA POR EXCESSO DE TENTATIVAS')
    print('')


