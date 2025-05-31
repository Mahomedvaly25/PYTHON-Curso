#Escreva um programa que converta uma temperatura digitada em graus celsius para graus Fahrenheit

c = float(input('Informe a temperatura em °C: '))
f = 9 * c /  5 + 32
print('A tempreratura de {} °C corresponde a {} °F!'.format(c,f))