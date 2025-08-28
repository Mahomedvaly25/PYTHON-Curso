''' Crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario e todos dicionarios
em uma lista. No final mostre:
a) Quantas pessoas foram cadastradas.
b) A Media de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da media.
'''

dados = list()
ficha = {}
resp = ''
mediaIdade = Mulheres = 0
while True:
    ficha['Nome'] = str(input('NOME: '))
    while True:
        ficha['Sexo'] = str(input('SEXO: [M / F]  ')).strip().upper()[0]
        if ficha['Sexo'] in 'MF':
            break
        print('ERRO: Responda apenas com [M / F] ')
    ficha['Idade'] = int(input('Idade: '))
    mediaIdade += ficha['Idade']
    dados.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S / N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N')
    if resp == "N":
        break
mediaIdade = mediaIdade / len(dados)

print('-=' * 20)
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
print('-=' * 20)
print(f'A Media de Idade = {mediaIdade:5.2f}')
print('-=' * 20)
for c in dados:
    if c['Sexo'] in 'Ff':
        print(f'As Mulheres cadastradas foram {c["Nome"]} |')
print('-=' * 20)
print(f'As Pessoas que estao acima da media sao:')
for i in dados:
    if i['Idade'] >= mediaIdade:
        print(f'   - {i["Nome"]} = {i["Idade"]}')
print('-=' * 30)
print('A Lista com todas as Pessoas Cadastradas:')
for p in dados:
    for i, p in p.items():
        print(f'   {i} = {p}')
    print()
