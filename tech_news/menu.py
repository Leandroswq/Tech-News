import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


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


def opcao_0():
    qtd = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(qtd)


def opcao_1():
    titulo = input("Digite o título: ")
    print("titulo")
    print(search_by_title(titulo))


def opcao_2():
    data = input("Digite a data no formato aaaa-mm-dd: ")
    print(search_by_date(data))


def opcao_3():
    tag = input("Digite a tag: ")
    print(search_by_tag(tag))


def opcao_4():
    categoria = input("Digite a categoria:")
    print(search_by_category(categoria))


def opcao_5():
    print(top_5_news())


def opcao_6():
    print(top_5_categories())


def opcao_7():
    print("Encerrando script")


# Requisito 12
def analyzer_menu():
    """Seu código deve vir aqui"""
    opcoes = {
        "0": opcao_0,
        "1": opcao_1,
        "2": opcao_2,
        "3": opcao_3,
        "4": opcao_4,
        "5": opcao_5,
        "6": opcao_6,
        "7": opcao_7,
    }
    print_menu()
    opcao = input("").strip()

    if opcao in opcoes:
        opcoes[opcao]()
    else:
        print("Opção inválida", file=sys.stderr)


if __name__ == "__main__":
    analyzer_menu()
