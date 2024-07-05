# Crie um sistema de e-commerce, onde o usuário possa, cadastrar-se
# Comprar um produto
# Descobrir o valor total
# pagar

print('Cadastro')
email = input('Digite seu Email: ') 
senha = int(input('Crie uma senha com 4 números: '))
print('')

print('Seja Bem Vindo')
email_entrada = input('Insira seu Email: ')
senha_entrada = int(input('Insira sua Senha: '))
print('')

if email == email_entrada and senha == senha_entrada:
    print('Escolha um produto')
    print('''
    0 - Carro R$ 12.000,00
    1 - Barco R$ 40.000,00
    2 - Avião R$ 1.000.000,00
    3 - Escavadeira R$ 500.000,00
    ''')
    produto = ['Carro', 'Barco', 'Avião', 'Escavadeira']
    valor = [12000, 40000, 1000000000, 500000]
    escolha, escolha2 = int(input('Selecione o número do item desejado: ')), int(input('Selecione o número do item desejado: '))
    print('')
    decidir = input('Deseja Verificar o carrinho  (sim/não): ')
    print('')
    if decidir == 'sim':
        print('Item selecionado >>>', produto[escolha],'e',produto[escolha2])
        variavel1 = valor[escolha] + valor[escolha2]
        print(f'Valor da Compra = R$ {float(variavel1):,.2f}')
        print('')
        dicidir2 = input('Deseja Efetuar a Compra (sim/não): ')
        print('')
        if dicidir2 == 'sim':
            print(f'''
            ---------------------------------------------
            | Obrigado Pela Confiança, Volte Sempre !!! |
            | Parabens pelo(a) {produto[escolha]} e {produto[escolha2]}            |
            ---------------------------------------------
            ''')
        else:
            print('Agradecemos sua Visita  (u_u)  espero que encontre o que precise')
    else:
        dicidir3 = input('Deseja Efetuar a Compra (sim/não): ')
        print('')
        if dicidir3 == 'sim':
            print(f'''
            ---------------------------------------------
            | Obrigado Pela Confiança, Volte Sempre !!! |
            | Parabens pelo(a) {produto[escolha]} e {produto[escolha2]}            |
            ---------------------------------------------
            ''')
        else:
            print('Agradecemos sua Visita  (u_u)  espero que encontre o que precise')        


elif email == email_entrada or senha == senha_entrada:
    print('')
    print('Seu Email ou senha estão incorretos, tente novamente')

else:
    print('')
    print('Você não está CADASTRADO')
    
