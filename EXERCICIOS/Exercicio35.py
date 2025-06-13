# CONDICOES EM PYTHON
# Densevolve um programa que leia o comprimento de 3 retas e diga aos usuarios se elas podem ou nao formar um triangulo.


print('-='*30)
print('ANALISADOR DE TRIANGULO')
print('-='*30)
r1 = float(input('Digite o 1o segmento: '))
r2 = float(input('Digite o 2o segmento: '))
r3 = float(input('Digite o 3o segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas esclolhidas \033[0;32mPODEM FORMAR UM TRIANGULO.\033[m')
else:
    print('As retas escolhidas \033[31mNAO PODEM FORMAR UM TRIANGULO.\033[m')