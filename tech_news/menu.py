def print_menu():
    menu = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""
    print(menu)


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    print_menu()


if __name__ == "__main__":
    analyzer_menu()
