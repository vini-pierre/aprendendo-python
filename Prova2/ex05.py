#5. Defina a função indices_pares que recebe como argumento uma lista de números inteiros 
#$w$ e devolve a lista dos elementos de $w$ em posições pares.

def indices_pares(x):
    return list(filter(lambda y : x.index(y) % 2 == 0, x))
    
print(indices_pares([4,3,7,1,2,9]))