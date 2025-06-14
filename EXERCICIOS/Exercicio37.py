# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario qual sera a base de conversao.
# -1 para binario
# -2 para octal
# -3 para hexadecimal
print('\033[33m-=\033[m'*20)
numero = int(input('Escolhe um Numero \033[4;35mQUALQUER:\033[m '))
print('\033[33m-=\033[m'*20)
print('''\033[4mDentre as opcoes escolhe uma das bases de conversao:
{}[1]{} Conversao para BINARIO
{}[2]{} Conversao para OCTAL
{}[3]{} Conversao para Hexadecimal'''.format('\033[31m','\033[m','\033[31m','\033[m','\033[31m','\033[m','\033[31m','\033[m','\033[31m','\033[m','\033[31m','\033[m'))
print('\033[33m+\033[m'* 30)
opcao = int(input('\033[31mESCOLHA SUA OPCAO\033[m: '))
print('\033[33m+\033[m'* 30)
if opcao == 1:
    print('\033[36m{}\033[m Convertidos para \033[4;35mBINARIA\033[m é igual a \033[7;32m{}\033[32m'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('\033[36m{}\033[m Convertidos para \033[4;35mOCTAL\033[m é igual a \033[7;32m{}\033[m'.format(numero, oct(numero)[2:]))
elif opcao ==3:
    print('\033[36m{}\033[m Convertidos para \033[4;35mHEXADECIMAL\033[m é igual a \033[7;32m{}\033[m'.format(numero, hex(numero)[2:]))
else:
    print('Numero \033[31minvalido\033[m, \033[32mTente Novamente\033[m.')
