''' Faca um programa que leia a media de um aluno, guardando tambem a situacao em um dicionario.
No final mostre o conteudo da estrutura na tela.'''

aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Qual media do {aluno["Nome"]}?  '))

if aluno['Media'] >= 7:
    aluno['Situacao'] = 'Aprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'Recuperacao'
else:
    aluno['Situacao'] = 'Reprovado'
print('-=' * 20)
for k,v in aluno.items():
    print(f'{k} = {v}')