idade = int(input('Digite é a sua idade: '))

if (idade <= 18):
    print('Menor de idade')
elif (idade > 18 and idade <= 65):
    print('Adulto')
elif (idade > 65 and idade <= 100):
    print('Maior de idade')
else:
    print('Centenário')