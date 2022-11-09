from tech_news.database import search_news
from datetime import datetime


def __get_title_and_url__(noticias):
    response = [(noticia["title"], noticia["url"]) for noticia in noticias]
    return response


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    noticias = search_news(query)
    response = __get_title_and_url__(noticias)
    return response


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Data inválida")
    date = date.strftime("%d/%m/%Y")
    query = {"timestamp": date}
    noticias = search_news(query)
    response = __get_title_and_url__(noticias)
    return response


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    query = {"tags": {"$regex": tag, "$options": "i"}}
    noticias = search_news(query)
    response = __get_title_and_url__(noticias)
    return response


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
