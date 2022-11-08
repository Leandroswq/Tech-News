import requests
from time import sleep
from parsel import Selector


# Requisito 1
def fetch(url: str) -> str:
    """Seu código deve vir aqui"""
    sleep(1)
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
    except requests.exceptions.ReadTimeout:
        return None
    if response.status_code != 200:
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    artigos = selector.css(".entry-preview")
    links = []
    for artigo in artigos:
        link = artigo.css("a::attr(href)").get()
        links.append(link)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    link = selector.css(".next::attr(href)").get()
    return link


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
