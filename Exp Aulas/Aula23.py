try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # Erro Generico
    print(f'O ERRO encontrado foi {erro.__cause__}')
except(ValueError, TypeError):
    print(f'Tivemos um problema com o tipo de dados que digitou!')
except ZeroDivisionError:
    print(f'Nao e possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print(f'O Usuario preferio nao informar os dados.')
else:
    print(f'O Resultado e {r:.1f}')
finally:
    print('Volte Sempre! Muito Obrigado.')