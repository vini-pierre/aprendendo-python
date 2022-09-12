class Item:
    def __init__(self, nome = '', preco = 0.0, estoque = 0):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque
        
    def __str__(self):
        preco = str(self.preco)
        estoque = str(self.estoque)
        return self.nome + " x " + estoque + " --> R$ " + preco 
    
class Pedido:
    def __init__(self, pagamento = ''):
        self.pagamento = pagamento
        self.total = 0

    def adicionaritens(self, item, qtd):
        self.total += item.preco * qtd
        item.estoque -= qtd
        
    def __str__(self):
        preco = str(self.preco)
        return self.nome + " x " + estoque + " --> R$ " + preco 

def main():
    objeto01 = Item('Arroz', 10.0, 30) 
    pedido = Pedido('debito')
    pedido.adicionaritens(objeto01, 10)

    print("--------------------")
    print("Supermecado do André")
    print("--------------------")
    print("")
    print(objeto01)
    print("")
    print("--------------------")
    print("Valor a ser pago: ",end="")
    print(pedido.total)
    print("--------------------")

if __name__ == '__main__':
    main()