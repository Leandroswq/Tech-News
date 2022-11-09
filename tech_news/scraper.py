import requests
from time import sleep
from parsel import Selector
import re
from tech_news.database import create_news


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
    response = {}

    selector = Selector(html_content)
    links = selector.css("link")
    for link in links:
        if link.css("link::attr(rel)").get() == "canonical":
            response["url"] = link.css("link::attr(href)").get()
            break

    summary = selector.css(".entry-content-wrap > .entry-content > p")
    response["summary"] = ("".join(summary[0].css("*::text").getall())).strip()

    header = selector.css("section.entry-header")
    response["title"] = header.css(".entry-title::text").get().rstrip()
    response["timestamp"] = header.css("li.meta-date::text").get()
    response["writer"] = header.css("span.author > a::text").get()
    comments_count = selector.css(".post-comments .title-block::text").get()
    if comments_count is not None:
        response["comments_count"] = int(re.findall("\d+", comments_count)[0])
    else:
        response["comments_count"] = 0

    response["tags"] = selector.css(".post-tags a::text").getall()
    response["category"] = header.css(".meta-category .label::text").get()
    return response


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    links_noticias = []

    homepage_url = "https://blog.betrybe.com/"
    while len(links_noticias) < amount:
        homepage_html = fetch(homepage_url)
        links_noticias.extend(scrape_novidades(homepage_html))
        homepage_url = scrape_next_page_link(homepage_html)

    links_noticias = links_noticias[:amount]

    noticias = [scrape_noticia(fetch(noticia)) for noticia in links_noticias]

    create_news(noticias)
    return noticias
