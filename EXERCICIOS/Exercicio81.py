# Crie um programa que vai ler varios numeros e colocar em uma lista, depois disso mostre:
# a) Quantos numeros foram digitados.
# b) A lista de valores, ordenada em ordem decrescente
# c) Se o valor 5 foi digitado e esta ou nao na lista.

quant = 0
list = []
while True:
    list.append(int(input('Digite um numero: ')))

    resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta invalida, Tente Novamente.')
        resp = str(input('Quer Continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

list.sort(reverse=True)
print(f'Voce digitou {len(list)} elementos.')
print(f'Os Valores em ordem Decrescente sao: {list}')
if 5 in list:
    print('O Valor (5) faz parte da lista.')
else:
    print('O Valor (5) nao foi encontrado na lista.')