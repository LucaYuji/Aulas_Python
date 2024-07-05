## Desafio 1

# VOCÊ É UM DEV E PRECISA CRIAR UM SISTEMA PARA UMA ESCOLA. 

# SISTEMA DE NOTAS DE ALUNOS QUE MOSTRE AS NOTAS DE ALUNOS, MÉDIA,  ALÉM DE MOSTRAR MENOR E A  MAIOR NOTA.

materia = input('Matéria: ')
nome = input('Nome do Aluno(a): ')
nota1 = float(input('Nota 1º Bimestre >>> ')) 
nota2 = float(input('Nota 2º Bimestre >>> '))
nota3 = float(input('Nota 3º Bimestre >>> '))
nota4 = float(input('Nota 4º Bimestre >>> '))

notas = []
notas.extend([nota1, nota2, nota3, nota4])
media = (sum(notas))/ int(len(notas))

resolucao = media >= 6
maior_nota = max(notas)
menor_nota = min(notas)

print(f'''
Matéria: {materia}
Aluno(a): {nome}
Média = {media:.2f}
Maior Nota = {maior_nota:.2f}
Menor Nota = {menor_nota:.2f}
Este aluno está aprovado?: {resolucao}
''')

