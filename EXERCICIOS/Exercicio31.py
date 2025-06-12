# CONDICOES EM PYTHON
# Densevolva um programa que pergunte a distancia de uma viagem em km.
# Calcule o preco da passagem, cobrando 0,50 cents por km para viagem ate 200 km e 0,45 cents para viagens mais longas.

print('*'*50)
distancia = float(input('Indique quantos Kms tem a viagem para calcular o seu Preco: '))
print('*'*50)
if distancia > 200:
    print('Conforme a distancia tera um custo de {} Euros tendo em consideracao o valor de 0,45 Cents por Kms'.format(distancia * 0.45))
else:
    print('Conforme a distancia tera um custo de {} Euros tendo em consideracao o valor de 0,50 Cents por Kms'.format(distancia * 0.50))

'''Ou podemos resolver o mesmo exercio de maneira simplificada:
preco = distancia * 0,50 if distancia <= 200 else distancia * 0,45
'''