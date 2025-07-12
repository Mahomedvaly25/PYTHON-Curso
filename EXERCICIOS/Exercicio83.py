# Crie um programa onde o usuario digite uma expressao qualquer que use parenteses.
# Seu aplicativo devera analisar se a expressao passada esta com parenteses aberto e fechados na ordem correta.

simbolos = []
expr = str(input('Digite uma EXPRESSAO Matematica qualquer: '))
for cont in expr:
    if cont == '(':
        simbolos.append('(')

    elif cont == ')':
        if len(simbolos) > 0:
            simbolos.pop()
        else:
            simbolos.append(')')
            break

if len(simbolos) == 0:
    print('A Expressao inserida esta CORRETA.')
else:
    print('A Expressao inserida esta ERRADA.')