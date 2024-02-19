from Objetos.cliente import cadastro, pedido_cadastro_cliente, pedido_cliente_existente, busca_cliente
from Objetos.produto import produto, busca_produto

def menu_principal():
    while True:
        print('\n Menu \n')
        print('1 - Cadastrar novo cliente, produto ou pedido')
        print('2 - Buscar clientes ou produtos')
        # print('3 - Criar novos pedidos associados a clientes existentes')
        print('3 - Sair \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao < 4:
                return opcao
            else:
                print('\n O valor inserido é inválido \n')
        else:
            print('\n O valor inserido é inválido \n')

def submenu_cadastro():
    while True:
        print('\n Submenu \n')
        print('1 - Cadastrar novo cliente')
        print('2 - Cadastrar novo produto')
        print('3 - Cadastrar novo pedido a um novo cliente')
        print('4 - Criar novos pedidos associados a clientes existentes')
        print('5 - Voltar ao menu principal \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 5:
                break
            elif opcao == 1:
                cadastro() 
            elif opcao == 2:
                produto()
            elif opcao == 3:
                pedido_cadastro_cliente() 
            elif opcao == 4:
                pedido_cliente_existente()
            else:
                print('\n O valor inserido é inválido \n')
        else:
            print('\n O valor inserido é inválido \n')

def submenu_busca():
    while True:
        print('\n Submenu \n')
        print('1 - Buscar cliente')
        print('2 - Buscar produto')
        print('3 - Voltar ao menu principal \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 3:
                break
            elif opcao == 1:
                busca_cliente()
            elif opcao == 2:
                busca_produto()
            else:
                print('\n O valor inserido é inválido \n')

        else:
            print('\n O valor inserido é inválido \n')
