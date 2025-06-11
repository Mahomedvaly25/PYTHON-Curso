# CONDICOES EM PYTHON
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre a menssagem dizendo que ele foi multado.
# A Multa vai custar 7.00 Euros por cada km acima do limiti.

velocidade = float(input('Digite a velocidade do carro: '))
kmUltrapassado = velocidade - 80
multa = kmUltrapassado * 7
if velocidade > 80:
    print('Atingiu o a velocidade superior a 80km/h.')
    print('-'*40)
    print('Tera de pagar uma multa de 7,00 euros a cada km ultrapassado.')
    print('-'*40)
    print('O total de km a mais foram: {}kms, e tera de pagar {}Euros'.format(kmUltrapassado,multa))
else:
    print('Velocidade dentro dos limites, Boa viagem!')