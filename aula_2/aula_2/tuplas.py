# TUPLE, imutável, não pode ser alterado
# não se pode adicionar nem remover itens da tupla

#conjuntos são mutaveis mas os dados são unicos, não se repetem conjunto = ser

# conjunto = list(range(1,150))
# print(conjunto)

menino = {
'nome' : 'Caio',
'idade' : 15,
'Graduação' : 'Eng',
'Solteiro' : True
}
nome = menino['nome']
print(nome)
print(menino.values())
print(menino.items())
print(menino.keys())

