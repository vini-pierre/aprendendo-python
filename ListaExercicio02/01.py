class item:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque

class pedido(item):
    def __init__(self, preco, estoque, quantidade):
        self.preco = preco
        self.estoque = estoque
        self.quantidade = quantidade

    def menos(self, estoque, quantidade):
        return 
