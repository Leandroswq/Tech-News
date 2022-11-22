# Projeto Tech News

Esse projeto foi desenvolvido durante meus estudos em python. Ele possui o objetivo de fazer uma raspagem de dados do [blog da Trybe](https://blog.betrybe.com/)

# Tecnologias utilizadas

* Python
* Extrair conteúdos de paginas html
* Armazenar dados no banco de dados

# Preview terminal interativo

![Imagem terminal interativo](img/terminal_iterativo.png)


# Como instalar as dependências

## 1 - Crie o ambiente virtual

~~~
python3 -m venv .venv
~~~

## 2 - Entre no ambiente virtual
~~~
source .venv/bin/activate
~~~

## 3 - Instale as dependências

Dependências de produção:

~~~
pip install -r requirements.txt
~~~

Dependências de produção e desenvolvimento:

~~~
pip install -r dev-requirements.txt
~~~

# Como executar

## 1 - Entre no ambiente virtual
Caso já esteja no ambiente virtual pode pular essa etapa
~~~
source .venv/bin/activate
~~~

## 2 - Rode a aplicação
A aplicação irá gerar um terminal interativo para auxiliar no uso da aplicação

~~~
python3 -m tech_news.main
~~~