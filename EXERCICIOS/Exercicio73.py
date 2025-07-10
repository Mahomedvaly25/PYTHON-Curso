# Crie uma tupla preenchida com os 20 primeiro colocados do ranking da UEFA de Futebol masculino, na ordem de colocacao . Depois mostre:
# a) Apenas os 5 primeiros colocados
# b) Os ultimos 4 colocados da tabela
# c) Uma lista com os times em ordem alfabetica
# d) Em que posicao na tabela esta o time Portugal?

equipas = ('inglaterra','Italia','Espanha','Alemanha','Franca','Paises-Baixo','Portugal',
           'Beilgica','Chequia','Turquia','Noruega','Grecia','Austria','Escocia',
           'Polonia','Dinamarca','Suica','Israel','Chipre','Suecia')
print(f'As Cinco primerira colocadas sao: \033[33m{equipas[:5]}\033[m')
print(f' Os Ultimos Quatro colocados sao: \033[32m{equipas[-4:]}\033[m')
print(f'As Equipas ordenadas sao:  \033[34m{sorted(equipas)}\033[m')
print(f'O Time de Portugal esta na posicao {equipas.index('Portugal')+1}')