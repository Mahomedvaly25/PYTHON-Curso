#     MANIPULACAO DE STRING
# Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Exemplo:
# 1984
# Unidade: 4
# Dezena: 8
# Centena: 9
# Milhar: 1

numero = int(input('Digite um Numero Qualquer de 1 a 9999:   '))
unidade = numero // 1 % 10   #Divisao inteira do numero com 1 e o resultado fazer o resto da divisao com 10
dezena = numero // 10 % 10   #Divisao inteira do numero com 10 e o resultado fazer o resto da divisao com 10
centena = numero // 100 % 10 #Divisao inteira do numero com 100 e o resultado fazer o resto da divisao com 10
Milhar = numero // 1000 % 10 #Divisao inteira do numero com 1000 e o resultado fazer o resto da divisao com 10
print('O numero digitado foi {} que corresponde a:')
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(Milhar))