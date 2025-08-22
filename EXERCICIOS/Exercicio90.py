''' Faca um programa que leia a media de um aluno, guardando tambem a situacao em um dicionario.
No final mostre o conteudo da estrutura na tela.'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Media: '))
situacao = ' '
if aluno['Media'] >= 7:
    situacao = 'AProvado'
if aluno['Media'] < 5:
    situacao = 'Reprovado'
if aluno['Media'] > 5 and aluno['Media'] < 7:
    situacao = 'Recuperacao'
print(f'{aluno},`{situacao}')