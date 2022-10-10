lista_2 = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 28}
]

so_nomes = map(lambda p: p['nome'], lista_2)
so_idades = map(lambda p: p['idade'], lista_2)
print(list(so_nomes))
print(list(so_idades))
