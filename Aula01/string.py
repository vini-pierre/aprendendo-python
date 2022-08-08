# print(dir(str))

nome = 'Vinicius Pierre' # string
print(nome)

print(nome[3]) # posição do vetor

print ("Vinicius Pierre" == 'Vinicius Pierre') 

texto = 'Texto entre apostrófos pode ter "aspas"' # pode usar aspas duplas dentro das aspas simples
print(texto)

doc = """texto com multiplas
linhas... """ # aspas triplas ele segue a quebra de linha

print(doc)

##########################
#   Exemplo

nome = 'Um nome qualquer'

print(nome[0])
print(nome[6])
print(nome[-3]) # pega os ultimos valores
print(nome[4:]) # pega os valores apartir do 4
print(nome[-5:]) # pega os ultimos 4 valores
print(nome[:4]) # pega 3 primeiros valores
print(nome[2:5]) # conjunto sempre aberto

##########################
# Exemplo 2

numero = '1234567890'

print(numero[::]) # imprime todos os valores
print(numero[::2]) # imprime de 2 em 2
print(numero[::-1]) # imprime todos os valores invertidos