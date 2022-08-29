from random import randint

sorteio = randint(0,9)
resposta = int(input('Digite um valor: '))

while resposta != sorteio:
    resposta = int(input('Digite um valor: '))


print(f'O número secreto {sorteio} foi encontrado') 