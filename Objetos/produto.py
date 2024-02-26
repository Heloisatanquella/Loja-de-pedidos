from Objetos.utils import buscar

produtos = []

class Produto: 

    def __init__(self, nome, descricao, preco, quantidade): 
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def dados_completos(self):
        print(f'\nNome do produto: {self.nome}; Descrição: {self.descricao}; Preço por unidade: {self.preco}; Quantidade disponível: {self.quantidade}\n')

    def linha(self):
        return f'{self.nome}|{self.descricao}|{self.preco}|{self.quantidade}\n'

def busca_produto():
    while True:
        nome = input('\n Digite o nome do produto: \n')
        produto = buscar(nome, produtos, 'nome')
        if isinstance (produto, Produto):
            produto.dados_completos()
            return produto
        else:
            print('\nNão encontrado\n')

def produto():

    while True:
        nome = input('Digite o nome do produto: \n')
        duplicado = buscar(nome, produtos, 'nome')

        if duplicado:
            print('Produto já existente. Tente novamente.')
        else:
            break

    descricao = input('Insira a descrição do produto: ')

    while True:
        preco = input('Insira o preço do produto (00.00): ')

        try:
            preco = float(preco)
            break
        except ValueError:
            print('\nO valor inserido não é válido \n')
            
    while True: 
        quantidade = input('Insira a quantidade em estoque: ')

        if quantidade.isdigit():
            quantidade = int(quantidade)
            break
        else:
            print('\nApenas valores inteiros serão aceitos \n')

    produto = Produto(nome, descricao, preco, quantidade)

    produtos.append(produto)
    print('\n Dados do produto cadastrado ')
    produto.dados_completos()
