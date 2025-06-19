# ESTRUTURA DE REPETICAO
s = 0
for cont in range(0,4):
    n = int(input('Digite um valor: '))
    s = s + n                   # ou podemos resumir esta expressao com s += n
print('O somatorio de todos os valores foi {}'.format(s))