# Densevolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# - A media de idade do grupo.
# - Qual e o nome do homem mais velho
# - Quantas mulheres tem com menos de 20 anos.

somaidade = 0
media = 0
homemvelho = 0
nomevelho = ''
mulhernova = 0
for c in range(1,4):
    print("----------- {}o PESSOA------------")
    nome = str(input('Digite seu nome completo: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().strip()
    somaidade = somaidade + idade
    if c == 1 and sexo in 'M,m':
        homemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo in 'F,f' and idade < 20:
        mulhernova += 1
media = somaidade / 4
print("A media de idade foi {}".format(media))
print('O Nome do homem mais velho e {} e tem {} Anos.'.format(nomevelho,homemvelho))
print('Foram {} mulheres novas do grupo.'.format(mulhernova))