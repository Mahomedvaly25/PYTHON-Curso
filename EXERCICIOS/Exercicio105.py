'''Faca um programa que tenha a funcao notas() que pode receber varias notas de alunos e vai retornar um dicionario com as seguintes informacoes:
- Quantidade de notas
- A Maior nota
- A Menor Nota
- A Media da turma
- A Situacao(Opcional)
- Adicione tambem as docstrings.'''

def notas(*n, sit=False):
    """
    -> Funcao para analisar notas e sutuacao de varios alunos.
    :param n: Uma ou mais notas dos alunos (aceita Varias).
    :param sit: Valor Opcional, que indica se deve ou nao mostrar a Situacao.
    :return: Dicionario com varios informacoes sobre a situacao da turma.
    """
    dic = {}
    dic['N. de Nota'] = len(n)
    dic['Maior Nota'] = max(n)
    dic['Menor Nota'] = min(n)
    dic['Media'] = sum(n)/len(n)
    if sit:
        if dic['Media'] >= 7:
            dic['Situacao'] = 'BOA'
        elif dic['Media'] >= 5:
            dic['Situacao'] = 'RAZOAVEL'
        else:
            dic['Situacao'] = 'RUIM'

    return dic

resp = notas(8,10,4,9, sit=True)
print(resp)
help(notas)
