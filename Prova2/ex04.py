#4. Defina a função quadrados_inv que recebe como argumento um número natural $n$ 
#devolve a lista dos $n$ primeiros quadrados perfeitos, por ordem decrescente.

def quadrados_inv(x):
    if x == 1:
        return x
    else:
        return x ** 2 

x = int(input('Digite o valor para : '))
print(list(reversed(list(map(lambda x : quadrados_inv(x), range(1,x+1))))))
