#3. Defina a função quadrados que recebe como argumento um número natural $n$ devolve a 
#lista dos $n$ primeiros quadrados perfeitos.

def quadrados(x):
    if x == 1:
        return x
    else:
        return x ** 2 

x = int(input('Digite o valor para : '))
print(list(map(lambda x : quadrados(x), range(1,x+1))))

