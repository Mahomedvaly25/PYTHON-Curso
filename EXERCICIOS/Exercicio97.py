'''Faca um programa que tenha uma funcao chamada escreva(), que receba um texto qualquer como parametro e mostre uma
mensagem com tamanho adaptavel.
Ex:
escreva('Ola, Mundo!')

Saida:
~~~~~~~~~~~~~~~
  Ola, Mundo!
~~~~~~~~~~~~~~~
'''

def escreva(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


titulo = str(input('Digite um Titulo qualquer: '))
escreva(titulo)
titulo = str(input('Outro Titulo: '))
escreva(titulo)