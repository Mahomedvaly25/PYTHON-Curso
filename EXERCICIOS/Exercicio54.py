# # Crie um programa que leia o ano de nascimento de sete pessoas, no final mostre quantas pessoas ainda nao atingiram a maioridade e quantas ja sao maiores.
from datetime import date
anoatual = date.today().year
idade = 0
maior = 0
menor = 0
for c in range(1,8):
    nascimento = int(input('Em que ano a {}a pessoa nasceu? '.format(c)))
    idade = anoatual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('''Com base nos dados colhidos:
 - {} pessoas ainda nao atingiram a maioridade
 - {} pessoas ja atingiram Maioridade.'''.format(menor,maior))
