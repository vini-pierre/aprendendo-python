lista_pessoas = [{'id': 1,'nome': 'Andre','idade': 30,'altura':1.83,'cursos':['C#', 'Python', 'Node']},
                {'id': 2,'nome': 'Ana','idade': 25,'altura':1.6,'cursos':['C#', 'Python', 'Node', 'C++']},
                {'id': 3,'nome': 'Bia','idade': 23,'altura':1.7,'cursos':['Python', 'Node']},
                {'id': 4,'nome': 'Guilherme','idade': 34,'altura':1.8,'cursos':['C#', 'Java', 'React']}]

for pessoa in lista_pessoas:
    for curso in pessoa['cursos']:
        nome = pessoa['nome']
        print(f'A pessoa {nome} faz o curso {curso}')