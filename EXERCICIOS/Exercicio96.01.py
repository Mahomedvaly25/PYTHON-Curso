def area(larg,comp):
    a = larg * comp
    print(f'A area de um terreno com {l} x {c} = {a} m2')
print('CONTROL DE TERRENOS')
print('-=' * 20)
l = float(input('(LARGURA) m2:  '))
c = float(input('(COMPRIMENTO) m2:  '))
print('-=' * 20)
area(l,c)