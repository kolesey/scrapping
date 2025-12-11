import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
URL = 'https://habr.com/ru/articles/'

response = requests.get(URL)

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

# Проходим по каждой статье на странице
for article in articles:
    date = article.find('time')['title'].split(',')[0]
    title = article.find('h2', class_='tm-title tm-title_h2').text
    link = 'https://habr.com' + article.find('a', class_='tm-title__link')['href']

    # Заходим по ссылке и получаем текст статьи.
    art_resp = requests.get(link)
    art_soup = BeautifulSoup(art_resp.text, 'html.parser')
    art_text = art_soup.find('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    art_content = art_text.text

    # Проверяем наличие хотя бы одного слова из списка
    for word in KEYWORDS:
        if (word in art_content) or (word in title):
            print(date, title, link, sep=' - ')
            break







