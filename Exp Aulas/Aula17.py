# Atributo para criacao de lista vazia
# 1o...
# valores = list()
# 2o...
valores = []

for cont in range(0,3):
    valores.append(int(input('Digite um valor: ')))
print('='*30)
for c,v in enumerate(valores):
    print(f'Na posicao {c} encontramos o valor {v}')
valores.sort()
valores.insert(0,9)
print('='*35)
print(f'Os Numeros digitados foram: {valores}')
print(f'Existem no total {len(valores)} elementos')
