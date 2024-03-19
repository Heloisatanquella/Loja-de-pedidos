from Objetos.utils import buscar
from Objetos.pedido import pedidos

clientes = []

class Cliente: #classe é o nosso objeto
    def __init__(self, nome, sobrenome, email, telefone): 
				#self é o próprio objeto, e precisa estar no metódo
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.telefone = telefone

    def dados_completos(self):
        print(f'\nNome completo: {self.nome} {self.sobrenome}; E-mail: {self.email}; Telefone: {self.telefone}\n')

    #formata a classe para salvar no arquivo
    def linha(self):
        return f'{self.nome}|{self.sobrenome}|{self.email}|{self.telefone}\n'

def busca_cliente():
    while True:
        email = input('\nDigite o e-mail do cliente: ')
        cliente = buscar(email, clientes, 'email')
        if isinstance(cliente, Cliente):
            cliente.dados_completos()
            return cliente
        else:
            print('\nNão encontrado')

def cadastro():
    
    nome = input('\nDigite o primeiro nome do cliente: ')
    sobrenome = input('Digite o sobrenome do cliente: ')
    
    while True:
        email = input('Insira o e-mail do cliente: ')
        duplicado = buscar(email, clientes, 'email')

        if duplicado:
            print('\nE-mail já cadastrado. Tente novamente. \n')
        else:
            break

    telefone = input('Insira o número para contato do cliente (DDD 9 9999.9999): ')

    cliente = Cliente(nome, sobrenome, email, telefone)

    clientes.append(cliente)
    print('\n Dados do cliente cadastrado \n')
    cliente.dados_completos()

    return cliente

def pedido_cliente_existente():
    cliente = busca_cliente()
    pedidos(cliente)

def pedido_cadastro_cliente():
    print('\nÉ necessário cadastrar um cliente \n')
    cliente = cadastro()
    pedidos(cliente)

