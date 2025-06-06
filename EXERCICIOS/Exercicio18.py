#Faca um programa que leia um angulo qualquer e mostre na tela o valor de seno, coseno e tangente desse angulo.
import math
Angulo = float(input('Digite um Angulo qualquer para ver o valor em SENO, COSSENO E TANGENTE: '))
seno = math.sin(math.radians(Angulo))
cosseno = math.cos(math.radians(Angulo))
tangente = math.tan(math.radians(Angulo))

print('O Angulo de {} tem um SENO de {:.2f}'.format(Angulo,seno))
print('Tem um COSSENO de {:.2f}'.format(cosseno))
print('Tem uma TANGENTE de {:.2f}'.format(tangente))