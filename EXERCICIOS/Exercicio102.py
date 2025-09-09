'''
Crie um programa que tenha uma funcao factorial() que receba 2 parametros:
O primeiro que indique o numero a calcular e o outro chamado show, que sera um valor logico(opcional), indicando
se sera mostrado ou nao na tela o processo de calculo do factorial.
'''

def factorial(n, show=False):
    """
    -> Calcule o Factorial de um Numero.
    :param n: O Numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O resultado do calculo de factorial de numero n.
    """
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


num = int(input('Quer Factorial de qual numero: '))
print(factorial(num, show=True))
help(factorial)
