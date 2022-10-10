#2. Defina a função soma_nat que recebe como argumento um número natural $n$ e devolve 
#a soma de todos os números naturais até $n$.

def soma_nat(x):
    if x == 1:
        return 1
    else:
        return x + soma_nat(x-1)

x = int(input('Digite o valor a ser somado: '))
print (soma_nat (x))