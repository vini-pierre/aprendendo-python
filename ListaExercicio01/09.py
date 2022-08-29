x = int(input("Número de entrada: "))

anterior = x
soma = x
proxima = x + soma 

for soma in range(0,11):
    print(f'{anterior}, ', end="")
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
