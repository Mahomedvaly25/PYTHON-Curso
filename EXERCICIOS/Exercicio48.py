#Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3 e que se encontram no intervalo de 1 a 500
soma = 0
totcont = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        soma += cont
        totcont += 1
print('No Total sao {} numeros IMPARES que sao DIVISIVEIS por 3, e a SOMA dos numeros e {}'.format(totcont,soma))