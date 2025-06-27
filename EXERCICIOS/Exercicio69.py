# Crie um programa que leia a idade e o Sexo de varias pessoas.
# A cada pessoa cadastrada o programa devera perguntar se o usuario quer ou nao continuar.
# No final Mostre:
# - Quantas pessoas tem mais de 18 Anos.
# - Quantos homens foram cadastrados
# - Quantas Mulheres com menos de 20 Anos.

idade = pessoas = pmais18 = tothomens = mulheres20 = 0
print(f'{"CADASTRE UMA PESSOA":^40}')
print('-='*20)
while True:
    sexo = resp = ' '
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO:[M/F] ')).strip().upper()[0]
    if idade > 18:
        pmais18 += 1
    if sexo == 'M':
        tothomens += 1
    if sexo == 'M' and idade < 20:
        mulheres20 += 1
    pessoas += 1
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{pessoas} Pessoas cadastradas e {pmais18} com mais de 18 anos')
print(f'Dentre eles foram {tothomens} Homens e {mulheres20} mulheres com menos de 20 anos')