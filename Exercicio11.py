#Faca um programa que leia a altura e largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintala, sabendo que cada litro de tinta pinta uma area de 2m quadrados.
print('='*50)
print('Para calcular a Area da parede deve fornencer os seguintes valores:')
Alt = float(input('- Qual a altura da parede: '))
Lar = float(input('- Qual a largura da parede: '))
A = Alt * Lar
Tn = A/2
print('='*50)
print('Area da parede: {:.3} m2'.format(A))
print('='*50)
print('Para pintar uma Area de {:.1f}m2 ira precisar de {:.1f} litros de tinta.'.format(A,Tn))