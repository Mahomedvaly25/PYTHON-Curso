# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta.
# No final mostre o boletim contendo a media de cada um, e permita que o usuario possa mostra as notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('Quer continuar: [S/N]  '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('-=' * 30)
while True:
    detalhes = int(input('Mostrar Notas de que Aluno? [999] para interroper: '))
    if detalhes == 999:
        break
    if detalhes <= len(ficha) - 1:
        print(f'Notas de {ficha[detalhes][0]} sao {ficha[detalhes][1]}')
    print('-' * 25)
