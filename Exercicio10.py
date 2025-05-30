#Crie um programa que leia quanto dinheiro um pessoa tem na carteira e mostre quantos dolares ela pode comprar.
print('='*60)
print('Cambio de:', end='  ')
print('1 Metical = 0.014 Euros')
MT = float(input('Informe quantos Meticais que converter para euros: '))
Eu = MT * 0.014
print('{} Mt = {} Eur'.format(MT,Eu))