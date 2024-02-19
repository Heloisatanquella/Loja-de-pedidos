def buscar(valor, lista, chave):
    for item in lista:
        if item[chave] == valor:
            return item
