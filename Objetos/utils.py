def buscar(valor, lista, chave):
    for item in lista:
        if getattr(item, chave) == valor:
            return item
