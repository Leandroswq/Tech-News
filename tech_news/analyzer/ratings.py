from tech_news.helpers.format_news import get_title_and_url
from tech_news.database import search_first__news_sorted


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    query = {}
    query_sort = ("comments_count", -1)
    noticias = search_first__news_sorted(query, query_sort, 5)
    response = get_title_and_url(noticias)
    return response


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
