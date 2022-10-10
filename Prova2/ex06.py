#6. Utilizando apenas função lambda e as funções map, reducee filter. Crie um script que some todas as 
#idades das pessoas com mais de 18 anos e menos que 30:

from functools import reduce


pessoas = [{'nome': 'Pedro', 'idade': 11},
        {'nome': 'Mariana', 'idade': 18},
        {'nome': 'Arthur', 'idade': 26},
        {'nome': 'Rebeca', 'idade': 6},
        {'nome': 'Raquel', 'idade': 34},
        {'nome': 'André', 'idade':22},
        {'nome': 'Tiago', 'idade': 19},
        {'nome': 'Gabriela', 'idade': 127}]

entre_18_e_30 = filter(lambda p: p['idade'] > 18 and p['idade'] < 30 , pessoas)
entre_18_e_30 = list(entre_18_e_30)

print(entre_18_e_30)
idades = reduce(lambda idade, pessoa: idade + pessoa['idade'], entre_18_e_30, 0)
print(idades)