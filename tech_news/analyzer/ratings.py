from tech_news.helpers.format_news import get_title_and_url
from tech_news.database import search_first__news_sorted, find_news


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
    noticias = find_news()
    categorias_contador = {}
    for noticia in noticias:
        categoria = noticia["category"]
        if categoria in categorias_contador:
            categorias_contador[categoria] += 1
        else:
            categorias_contador[categoria] = 1
    categorias = [categoria for categoria in categorias_contador]
    categorias.sort(
        key=lambda categoria: (categorias_contador[categoria] * -1, categoria),
        reverse=False,
    )
    if len(categorias) >= 5:
        return categorias[:5]
    else:
        return categorias
