#1 . Defina a função fibonacci que recebe como argumento um número natural $n$ e devolve o 
#$n$-ésimo número da sucessão de Fibonacci. Recorde que a sucessão dos números de 
#Fibonacci é definida recursivamente como se segue:

def fibonacci (w, x = 0, y = 1):
  if w == 0:
    return x
  else:
    return fibonacci (w - 1, y, x + y)

x = int(input('Digite uma posição da Fibonacci: '))
print (fibonacci (x-1))