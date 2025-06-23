# Crie um programa que leie varios numeros inteiros pelo teclado.
# O programa so vai parar quando usuario digitar o valor 999, que e a condicao de parada.
# No Final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag.)
soma = c = 0
n = int(input('Digite um numero: '))
while n != 999:
    soma += n
    n = int(input('Digite outro numero para somar: '))
    c += 1
print('Voce digitou {} valores, e a soma entre eles = {}'.format(c,soma))
