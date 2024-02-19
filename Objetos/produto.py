from Objetos.helper import buscar


produtos = []

def busca_produto():
    while True:
        nome = input('Digite o nome do produto: ')
        produto = buscar(nome, produtos, 'nome')
        if produto:
            print(produto)
            return produto
        else:
            print('Não encontrado')

def produto():
    produto = {}

    while True:
        nome = input('Digite o nome do produto: ')
        duplicado = buscar(nome, produtos, 'nome')

        if duplicado:
            print('Produto já existente. Tente novamente.')
        else:
            produto['nome'] = nome
            break

    produto['descrição'] = input('Insira a descrição do produto: ')

    while True:
        preco = input('Insira o preço do produto (00.00): ')

        try:
            produto['preço'] = float(preco)
            break
        except ValueError:
            print('\nO valor inserido não é válido \n')
            
    while True: 
        quantidade = input('Insira a quantidade em estoque: ')

        if quantidade.isdigit():
            produto['quantidade'] = int(quantidade)
            break
        else:
            print('\nApenas valores inteiros serão aceitos \n')

    produtos.append(produto)
    print('\n Dados do produto cadastrado \n')
    print(produto)
