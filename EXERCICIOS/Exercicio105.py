def voto(ano):
    from datetime import date
    actual = date.today().year
    idade = actual - ano
    if idade <= 16 < 18 or idade > 65:
        print(f'Idade de {idade} = Voto Opcional')
    elif idade < 16:
        print(f'Idade de {idade} = Nao tem idade para Voto')
    else:
        print(f'Idade de {idade} = Voto Obrigatorio.')

nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))