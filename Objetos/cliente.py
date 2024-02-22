from Objetos.helper import buscar
from Objetos.pedido import pedidos

clientes = []

def busca_cliente():
    while True:
        email = input('\nDigite o e-mail do cliente: ')
        cliente = buscar(email, clientes, 'e-mail')
        if cliente:
            print(cliente)
            return cliente
        else:
            print('Não encontrado')

def cadastro():
    cliente = {}

    cliente['nome'] = input('\nDigite o primeiro nome do cliente: ')
    cliente['sobrenome'] = input('Digite o sobrenome do cliente: ')
    
    while True:
        email = input('Insira o e-mail do cliente: ')
        duplicado = buscar(email, clientes, 'e-mail')

        if duplicado:
            print('\nE-mail já cadastrado. Tente novamente. \n')
        else:
            cliente['e-mail'] = email
            break

    cliente['telefone'] = input('Insira o número para contato do cliente (DDD 9 9999.9999): ')

    clientes.append(cliente)
    print('\n Dados do cliente cadastrado \n')
    print(cliente)

    return cliente

def pedido_cliente_existente():
    cliente = busca_cliente()
    pedidos(cliente)

def pedido_cadastro_cliente():
    print('\nÉ necessário cadastrar um cliente \n')
    cliente = cadastro()
    pedidos(cliente)

