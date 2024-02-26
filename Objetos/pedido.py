from Objetos.produto import busca_produto
lista_pedidos = []

class Pedido:
      
    def __init__(self, produtos, total_do_pedido, cliente):
        self.produtos = produtos
        self.total_do_pedido = total_do_pedido
        self.cliente = cliente

    def dados_pedido(self):
        print(f'\nProdutos adicionados ao pedido: {self.produtos}; Valor total do pedido: {self.total_do_pedido}; Comprador: {self.cliente}\n')

    def linha(self):
        produtos = []

        for item in self.produtos:
            nome = item['nome']
            quantidade = item['quantidade']
            total = item['total']
            produto_linha = f'{nome}:{quantidade}:{total}'
            produtos.append(produto_linha)

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
        produtos.append(item)
    
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
