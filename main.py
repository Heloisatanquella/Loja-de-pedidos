from Objetos.menus import menu_principal, submenu_busca, submenu_cadastro
from manipulador_arquivos import read, save

def main():
    #leitura dos arquivos ao iniciar o programa
    read()

    # print(clientes)
    # print(produtos)
    # print(lista_pedidos)

    while True:
        opcao = menu_principal()
        if opcao == 1:
            submenu_cadastro()
        
        elif opcao == 2:
            submenu_busca()

        elif opcao == 3:
            break
    #Salvamento dos arquivos ao encerrar o programa
    save()

main()

   