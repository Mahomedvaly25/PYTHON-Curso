# Refaca o Desafio 35 dos Triangulos, acrescentando o recurso de que tipo de triangulo sera formado:
# - EQUILATERO - todos os lados iguais
# - ISOSCELES - dois lados iguais
# - ESCALENO - todos os lados diferentes

print('-='*30)
print('ANALISADOR DE TRIANGULO')
print('-='*30)
r1 = float(input('Digite o 1o segmento: '))
r2 = float(input('Digite o 2o segmento: '))
r3 = float(input('Digite o 3o segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas esclolhidas \033[0;32mPODEM FORMAR UM TRIANGULO', end=' ')
    if r1 == r2 == r3:
        print('EQUILATERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISOSCELES.')
else:
    print('As retas escolhidas \033[31mNAO PODEM FORMAR UM TRIANGULO.\033[m')