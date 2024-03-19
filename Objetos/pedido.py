from Objetos.produto import busca_produto
lista_pedidos = []

class Item_Pedido:

    def __init__(self, nome, quantidade, total):
        self.nome = nome
        self.quantidade = quantidade
        self.total = total

    def dados_item(self):
        print(f'\nItem: {self.nome} - Quantidade: {self.quantidade} - Total: R${self.total}')

    def linha(self):
        return f'{self.nome}:{self.quantidade}:{self.total}'

class Pedido:
      
    def __init__(self, produtos, total_do_pedido, cliente):
        self.produtos = produtos
        self.total_do_pedido = total_do_pedido
        self.cliente = cliente

    def dados_pedido(self):
        print(f'\nProdutos adicionados ao pedido:')
        for produto in self.produtos:
            if isinstance(produto, Item_Pedido):
                produto.dados_item()
        print(f'\nValor total do pedido: {self.total_do_pedido}; Comprador: {self.cliente}\n')

    def linha(self):
        produtos = []

        for item in self.produtos:
            if isinstance(item, Item_Pedido):
                produtos.append(item.linha())

#sublinha de itens do pedido
        produtos = '/'.join(produtos)
        return f'{self.cliente}|{self.total_do_pedido}|{produtos}\n'

def pedidos(cliente):

    produtos = []
    total_do_pedido = 0
    cliente = cliente.email

    while True:
        #produto referente ao pedido
        item = {}
        #referencia do produto no estoque
        produto = {}

        while True:
            produto = busca_produto()
            if produto:
                item['nome'] = produto.nome
                break

        while True:
            quantidade = input('Digite a quantidade: ')

            if quantidade.isdigit():
                quantidade = int(quantidade)
                if quantidade <= produto.quantidade:
                    produto.quantidade = produto.quantidade - quantidade
                    item['quantidade'] = quantidade
                    break
                else:
                    print('\nEstoque insuficiente \n')
            else:
                print('\nApenas valores inteiros serão aceitos \n')

        item['total'] = produto.preco * item['quantidade']
        total_do_pedido = total_do_pedido + item['total']
        item_pedido = Item_Pedido(item['nome'], item['quantidade'], item['total'])
        produtos.append(item_pedido)
    
        print('Cadastrar mais produtos? \n')
        print('1: Sim \n')
        print('2: Não \n')

        novo = 1
        while True:  
            novo = input()

            if novo.isdigit():
                novo = int(novo)
                if novo == 2:
                    pedido = Pedido(produtos, total_do_pedido, cliente)
                    lista_pedidos.append(pedido)
                    pedido.dados_pedido()
                    return pedido
                elif novo == 1:
                    print(item)
                    break
                else:
                    print('\nValor inválido \n')
            
            else:
                print('\nApenas valores inteiros serão aceitos \n')

#FIXME: resolver o problema abaixo
# class Desenho:
    
#     def desenhar_quadrado(self):
#         pass

#     def desenhar_circulo(self):
#         pass

#     def desenhar_retangulo(self):
#         pass