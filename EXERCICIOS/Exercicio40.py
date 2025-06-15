# Crie um programa que leia 2 notas de um aluno e calcule sua media, mostrando uma menssagem no final, de acordo com a media atingida:
# - Media abaixo de 5.0:
#    REPROVADO
# - Media entre 5.0 a 6.9:
#    RECUPERACAO
# - Media 7.0 ou superior:
#    APROVADO

nota1 = float(input('Digite a 1o Nota: '))
nota2 = float(input('Digite a 2a Nota: '))
media = ( nota1 + nota2 ) / 2
print('A Media das duas Notas é {}'.format(media))
if media <= 5 and media >= 7:
    print('Precisa de RECUPERACAO')
elif media <= 5:
    print('Esta REPROVADO')
else:
    print('APROVADO, Parabens...')
