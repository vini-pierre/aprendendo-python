class Contato:
    def __init__(self, nome, numero, email):
        self.nome = nome
        self.numero = numero
        self.email = email

class Agenda:
    def __init__(self, contato = []):
        self.contato = contato

    def addlista(self, contatonovo):
        self.contato.append(contatonovo)


def main():
    contato1 = Contato('Diego Calciolari', 19984188133, 'marilinda@gmail.com')
    contato2 = Contato('Mariana Rubim', 11982245229, 'diloko@gmail.com')
    contato3 = Contato('João Guilherme', 19999188711, 'joana@gmail.com')

    agenda = Agenda([])
    agenda.addlista(contato1)
    agenda.addlista(contato2)
    agenda.addlista(contato3)

    print("Agenda:")
    print("--------------------")
    print(f'Nome: {agenda.contato[0].nome}, Número: {agenda.contato[0].numero}, Email: {agenda.contato[0].email}')
    print("--------------------")
    print(f'Nome: {agenda.contato[1].nome}, Número: {agenda.contato[1].numero}, Email: {agenda.contato[1].email}')
    print("--------------------")
    print(f'Nome: {agenda.contato[2].nome}, Número: {agenda.contato[2].numero}, Email: {agenda.contato[2].email}')
    print("--------------------")

if __name__ == '__main__':
    main()