'''
Crie um programa que tenha uma funcao factorial() que receba 2 parametros:
O primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional), indicando
se sera mostrado ou nao na tela o processo de calculo do factorial.
'''

def factorial(n, show=False):
    f = 1
    for c in range(n , 0 , -1):
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(f' x ', end=' ')
            else:
                print(f' = ', end=' ')
        f *= c
    return f


print(factorial(5, show=True))
