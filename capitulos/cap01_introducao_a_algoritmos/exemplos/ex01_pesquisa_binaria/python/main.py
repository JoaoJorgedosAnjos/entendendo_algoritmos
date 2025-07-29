def pesquisa_binaria(lista: list[int], item: int) -> int:
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:  
            baixo = meio + 1
    return None

if __name__ == "__main__":
    minha_lista = [1, 3, 5, 7, 9]

    print(f"Buscando 7 em {minha_lista}: {pesquisa_binaria(minha_lista, 7)}")    # Expected: 3
    print(f"Buscando 1 em {minha_lista}: {pesquisa_binaria(minha_lista, 1)}")    # Expected: 0
    print(f"Buscando 9 em {minha_lista}: {pesquisa_binaria(minha_lista, 9)}")    # Expected: 4
    print(f"Buscando 0 em {minha_lista}: {pesquisa_binaria(minha_lista, 0)}")    # Expected: -1
    print(f"Buscando 6 em {minha_lista}: {pesquisa_binaria(minha_lista, 6)}")    # Expected: -1
    print(f"Buscando 10 em {minha_lista}: {pesquisa_binaria(minha_lista, 10)}")  # Expected: -1

    outra_lista = [2, 4, 6, 8, 10, 12, 14, 16]
    print(f"Buscando 8 em {outra_lista}: {pesquisa_binaria(outra_lista, 8)}") # Expected: 3
    print(f"Buscando 15 em {outra_lista}: {pesquisa_binaria(outra_lista, 15)}") # Expected: -1