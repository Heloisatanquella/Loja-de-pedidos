from Objetos.produto import busca_produto
lista_pedidos = []

def pedidos(cliente):
    pedido = {}
    pedido['produtos'] = []
    pedido['total_do_pedido'] = 0
    pedido['cliente'] = cliente['e-mail']

    while True:
        #produto referente ao pedido
        item = {}
        #referencia do produto no estoque
        produto = {}

        while True:
            produto = busca_produto()
            if produto:
                item['nome'] = produto['nome']
                break

        while True:
            quantidade = input('Digite a quantidade: ')

            if quantidade.isdigit():
                quantidade = int(quantidade)
                if quantidade <= produto['quantidade']:
                    produto['quantidade'] = produto['quantidade'] - quantidade
                    item['quantidade'] = quantidade
                    break
                else:
                    print('\nEstoque insuficiente \n')
            else:
                print('\nApenas valores inteiros serão aceitos \n')

        item['total'] = produto['preço'] * item['quantidade']
        pedido['total_do_pedido'] = pedido['total_do_pedido'] + item['total']
        pedido['produtos'].append(item)
        print(item)

        print('Cadastrar mais produtos? \n')
        print('1: Sim \n')
        print('2: Não \n')

        novo = 1
        while True:  
            novo = input()

            if novo.isdigit():
                novo = int(novo)
                if novo == 2:
                    print(pedido)
                    lista_pedidos.append(pedido)
                    return pedido
                elif novo == 1:
                    print(item)
                    break
                else:
                    print('\nValor inválido \n')
            
            else:
                print('\nApenas valores inteiros serão aceitos \n')
