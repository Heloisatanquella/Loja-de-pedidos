from Objetos.cliente import clientes
from Objetos.produto import produtos
from Objetos.pedido import lista_pedidos

#função de salvamento de todos os arquivos, que é chamada na main
def save():
    save_cliente(clientes)
    save_produto(produtos)
    save_pedido(lista_pedidos)

#função de leitura de todos os arquivos, que é chamada na main
def read():
    read_cliente()
    read_produto()
    read_pedido()

def save_cliente(clientes):
    arquivo = open('dados_clientes.txt', 'w')
    for cliente in clientes:
        nome = cliente['nome']
        sobrenome = cliente['sobrenome']
        email = cliente['e-mail']
        telefone = cliente['telefone']

        linha = f'{nome}|{sobrenome}|{email}|{telefone}\n'
        arquivo.write(linha)

    arquivo.close()

def read_cliente():
    arquivo = open('dados_clientes.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.split('|')
        cliente = {}
        cliente['nome'] = dados[0]
        cliente['sobrenome'] = dados[1]
        cliente['e-mail'] = dados[2]
        #replace para esconder o \n
        cliente['telefone'] = dados[3].replace('\n', '')
        clientes.append(cliente)

    arquivo.close()

def save_produto(produtos):
    arquivo = open('dados_produtos.txt', 'w')
    for produto in produtos:
        nome = produto['nome']
        descricao = produto['descrição']
        preco = produto['preço']
        quantidade = produto['quantidade']

        linha = f'{nome}|{descricao}|{preco}|{quantidade}\n'
        arquivo.write(linha)

    arquivo.close()

def read_produto():
    arquivo = open('dados_produtos.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.split('|')
        produto = {}
        produto['nome'] = dados[0]
        produto['descrição'] = dados[1]
        produto['preço'] = float(dados[2])
        produto['quantidade'] = int(dados[3].replace('\n', ''))
        produtos.append(produto)

    arquivo.close()

def save_pedido(pedidos):
    arquivo = open('dados_pedidos.txt', 'w')
    for pedido in pedidos:
        cliente = pedido['cliente']
        total_do_pedido = pedido['total_do_pedido']
        produtos = []

        for produto in pedido['produtos']:
            nome = produto['nome']
            quantidade = produto['quantidade']
            total = produto['total']
            produto_linha = f'{nome}:{quantidade}:{total}'
            produtos.append(produto_linha)

        produtos = '/'.join(produtos)
        linha = f'{cliente}|{total_do_pedido}|{produtos}\n'
        arquivo.write(linha)

    arquivo.close()

def read_pedido():
    arquivo = open('dados_pedidos.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        pedido = {}
        dados = linha.split('|')
        pedido['cliente'] = dados[0]
        pedido['total_do_pedido'] = float(dados[1])
        pedido['produtos'] = []

        produtos = dados[2].replace('\n', '').split('/')
        for linha_produto in produtos:
            produto = {}
            item = linha_produto.split(':')
            produto['nome'] = item[0]
            produto['quantidade'] = int(item[1])
            produto['total'] = float(item[2])
 
            pedido['produtos'].append(produto)

        lista_pedidos.append(pedido)

    arquivo.close()