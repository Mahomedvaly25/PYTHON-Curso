# CONDICOES EM PYTHON
# Faca um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ANO qualquer para saber se é BISSEXTO: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #se o ano for divisivel por 4 e nao divisivel por 100 ou divisivel por 400
    print('O ANO de {} é BISSEXTO'.format(ano))
else:
    print('O ANO de {} nao é BISSEXTO'.format(ano))