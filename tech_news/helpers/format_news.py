def get_title_and_url(noticias):
    response = [(noticia["title"], noticia["url"]) for noticia in noticias]
    return response
