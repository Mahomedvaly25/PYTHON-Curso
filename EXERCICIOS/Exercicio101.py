'''
Crie um programa que tenha uma funcao chamada voto() que vai receber como parametro o ano de nascimento de uma pessoa,
retornando o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO  nas eleicoes.
'''

def voto(ano):
    from datetime import date
    actual = date.today().year
    idade = actual - ano
    if idade <= 16 < 18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional!'
    elif idade < 16:
        return f'Com {idade} anos: NAO VOTA!'
    else:
        return f'Com {idade} anos: Voto Obrigatorio!'


nasc = int(input('Ano Nascimento: '))
print(voto(nasc))