'''Faca um programa que tenha uma funcao chamada àrea(). Que receba as dimensoes de um terreno retangular(largura e
comprimento) e mostre a àrea do terreno.
'''
def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno com {larg} x {comp} e de {a} m2.')

print('-=' * 14)
print('    CONTROL DE TERRENOS')
print('-=' * 14)
l = float(input('(LARGURA) m2:  '))
c = float(input('(COMPRIMENTO) m2:  '))
print('-=' * 24)
area(l,c)