from tech_news.menu import analyzer_menu


def main():
    continue_loop = True

    while continue_loop:
        opcao = analyzer_menu()
        if opcao == "7":
            continue_loop = False


if __name__ == "__main__":
    main()
