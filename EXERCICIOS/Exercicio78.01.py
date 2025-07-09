# Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final mostre qual maior e o menor digitado e as suas respetivas posicoes na lista.
mai = men = 0
x = []
for c in range(0,5):
    x.append(int(input(f'Digite um numero na posicao {c}: ')))
    if c == 0:
        mai = men = x[c]
    else:
        if x[c] > mai:
            mai = x[c]
        if x[c] < men:
            men = x[c]

print(f'O Maior valor digitado foi {mai}, na Posicao ',end=' ')
for pos , val in enumerate(x):
    if val == mai:
        print(pos, end=" ")
print()
print(f'O Menor valor digitado foi {men}, na Posicao ',end=' ')
for pos , val in enumerate(x):
    if val == men:
        print(pos)
