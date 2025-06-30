from re import findall

from django.contrib.sitemaps.views import index

equipas = ('inglaterra','Italia','Espanha','Alemanha','Franca','Paises-Baixo','Portugal',
           'Beilgica','Chequia','Turquia','Noruega','Grecia','Austria','Escocia',
           'Polonia','Dinamarca','Suica','Israel','Chipre','Suecia')
print('-='*20)
print('OS CINCO PRIMEIROS COLOCADOS SAO:')
print('-='*20)
for p,pricolocados in enumerate(equipas[0:5]):
    print(f'{p+1} o. Colocado', pricolocados)
print('-='*20)

print('OS ULTIMOS QUATRO COLOCADOS SAO:')
print('-='*20)
for pricolocados in equipas[-4:]:
    print(equipas.index(pricolocados)+1,'o. Colocado', pricolocados)
print('-='*20)
print('EM ORDEM ALFABETICA:')
print('-='*80)
print(sorted(equipas))
print('-='*80)
print(f'O Time de Portugal esta na {equipas.index('Portugal')+1}a Posicao')