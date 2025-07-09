# Crie um programa onde o usuario pode digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero ja exista la dentro, ele nao sera adicionado.
# No Final serao exibidos todos os valores unicos digitados em ordem crescente.

resp = 'S'
num = []
while True:
    n = int(input('Digite um numero: '))
    if n not in num:
        num.append(n)
        print('Adicionao com sucesso...')
    else:
        print('Numero repetido, Tente Novamente: ')

    resp = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    while resp not in 'SN':
        print('Resposta ERRADA, Tente Novamente.')
        resp = str(input('Quer continuar: [S/N]')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Digitou os valores: {sorted(num)}')
