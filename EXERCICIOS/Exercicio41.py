# A Confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com idade:
# - Ate 9 Anos: MIRIM
# - Ate 14 Anos: INFANTIL
# - Ate 19 Anos: JUNIOR
# - Ate 20 Anos: SENIOR
# - Acima: MASTER

from datetime import date
anoAtual = date.today().year
anoNasc = int(input('Indique o Ano de Nascimento do ATLETA: '))
idade = anoAtual - anoNasc
print('O Atleta tem {} Anos de IDADE'.format(idade))
if idade <= 9:
    print('Classificacao: MERIM')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 20:
    print('Classificacao: SENIOR')
else:
    print('Classificacao: MASTER')
