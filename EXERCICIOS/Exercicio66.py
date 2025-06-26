# Crie um programa que leia varios numeros inteiros pelo teclado.
# O Programa so vai parar quando o usuario digitar valor 999, que e a condicao de parada.
# No Final mostre quantos numeros foram digitados e qual foi a soma entre eles (disconsideranco o flag).

totalnumero = soma = 0
while  True:
    n = int(input('Digite um numero, ou [999 para PARAR]: '))
    if n == 999:
        break
    totalnumero += 1
    soma += n
print(f'Foram digitados {totalnumero}, e a Soma = {soma}')
