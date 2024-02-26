from Objetos.cliente import clientes, Cliente
from Objetos.produto import produtos, Produto
from Objetos.pedido import lista_pedidos, Pedido

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
        linha = cliente.linha()
        arquivo.write(linha)

    arquivo.close()

def read_cliente():
    arquivo = open('dados_clientes.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.split('|')
        nome = dados[0]
        sobrenome = dados[1]
        email = dados[2]
        #replace para esconder o \n
        telefone = dados[3].replace('\n', '')

        cliente = Cliente(nome, sobrenome, email, telefone)
        clientes.append(cliente)

    arquivo.close()

def save_produto(produtos):
    arquivo = open('dados_produtos.txt', 'w')
    for produto in produtos:
        linha = produto.linha()
        arquivo.write(linha)

    arquivo.close()

def read_produto():
    arquivo = open('dados_produtos.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        dados = linha.split('|')
        produto = {}
        nome = dados[0]
        descricao = dados[1]
        preco = float(dados[2])
        quantidade = int(dados[3].replace('\n', ''))

        produto = Produto(nome, descricao, preco, quantidade)
        produtos.append(produto)

    arquivo.close()

def save_pedido(pedidos):
    arquivo = open('dados_pedidos.txt', 'w')
    for pedido in pedidos:
        linha = pedido.linha()
        arquivo.write(linha)

    arquivo.close()

def read_pedido():
    arquivo = open('dados_pedidos.txt', 'r')
    linhas = arquivo.readlines()
    for linha in linhas:
        pedido = {}
        dados = linha.split('|')
        print(dados)
        cliente = dados[0]
        total_do_pedido = float(dados[1])
        produtos = []

        produtos_linha = dados[2].replace('\n', '').split('/')
        for linha_produto in produtos_linha:
            produto = {}
            item = linha_produto.split(':')
            produto['nome'] = item[0]
            produto['quantidade'] = int(item[1])
            produto['total'] = float(item[2])
 
            produtos.append(produto)

        pedido = Pedido(produtos, total_do_pedido, cliente)
        lista_pedidos.append(pedido)

    arquivo.close()