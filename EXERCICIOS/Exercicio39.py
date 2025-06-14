# Faca uma programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar  ao servico militar.
# - Se é a hora de se alistar.
# - Se ja possui o tempo de alistamento.
# Seu programa tambem devera mostrar o campo qu falta ou que ja passou do prazo.

from datetime import date

anoActual = date.today().year
anoNasc = int(input('Digite o Ano em que Nasceu: '))

idade = anoActual - anoNasc
print('Quem nasceu em {}, tem {} Anos de idade em {}'.format(anoNasc,idade,anoActual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE.')
elif idade < 18:
    saldo = 18 - idade
    ano = anoActual + saldo
    print('Ainda faltam {} anos para se alistar.'.format(saldo))
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = anoActual - saldo
    print('Voce ja devia ter se alistado a {} Anos.'.format(saldo))
    print('Seu alistamento seria em {}'.format(ano))
