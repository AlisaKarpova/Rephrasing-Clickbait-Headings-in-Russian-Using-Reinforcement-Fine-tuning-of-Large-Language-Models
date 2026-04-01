"""

# Интерфакс (главные события) - всего 2010
"""

import requests
from bs4 import BeautifulSoup

news_titles = []
url = 'https://www.interfax-russia.ru/moscow/main?per-page=2004'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_ ="d-block d-md-none mt-20")
for title in titles:
  title = title.find('span', class_="h3 mb-15")
  news_titles.append(title.text)

with open('interfax', 'w', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""# Lenta.ru (политика + новости - моя страна + культура + криминал) - всего 1484

Политика - Россия и мир
"""

url = 'https://lenta.ru/rubrics/russia/politic/'
urls1 = []
for i in range(1, 8):
  new_url = url + str(i) + '/'
  urls1.append(new_url)

url = 'https://lenta.ru/rubrics/world/politic/'
urls2 = []
for i in range(1, 8):
  new_url = url + str(i) + '/'
  urls2.append(new_url)

urls = urls1 + urls2

news_titles = []
for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  titles = soup.find_all('a', class_="card-full-news _subrubric")
  for title in titles:
    title = title.find('h3',  class_="card-full-news__title")
    if title.text not in news_titles:
      news_titles.append(title.text)

with open('lenta', 'w', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""Новости - моя страна"""

news_titles = []
url = 'https://lenta.ru/rubrics/mycountry/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.find_all('div', class_="card-mini__text")
for title in titles:
  title = title.find('h3', class_="card-mini__title")
  news_titles.append(title.text)

with open('lenta', 'a', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""Культура"""

url = 'https://lenta.ru/rubrics/culture/art/'
urls1 = []
for i in range(1, 8):
  new_url = url + str(i) + '/'
  urls1.append(new_url)

news_titles = []
for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  titles = soup.find_all('a', class_="card-full-news _subrubric")
  for title in titles:
    title = title.find('h3',  class_="card-full-news__title")
    if title.text not in news_titles:
      news_titles.append(title.text)

with open('lenta', 'a', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""Криминал"""

url = 'https://lenta.ru/rubrics/forces/violation/'
urls1 = []
for i in range(1, 8):
  new_url = url + str(i) + '/'
  urls1.append(new_url)

news_titles = []
for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  titles = soup.find_all('a', class_="card-full-news _subrubric")
  for title in titles:
    title = title.find('h3',  class_="card-full-news__title")
    if title.text not in news_titles:
      news_titles.append(title.text)

with open('lenta', 'a', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""# Woman.ru (реальная жизнь) - 3425"""

url = 'https://www.woman.ru/real-life/page-'
urls = []
for i in range(1, 203):
  new_url = url + str(i) + '/'
  urls.append(new_url)

news_titles = []
for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  titles = soup.find_all('span', class_="announce-inline__title mt-2 mt-d-0 mb-1")
  for title in titles:
    title = title.find(class_="announce-inline__title-link")
    if title.text not in news_titles:
      news_titles.append(title.text)

with open('Woman', 'w', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')

"""# Forbes (бизнес) - 1194 (сайт блокирует доступ)


"""

import time

"""Страницы 1 - 20"""

url = 'https://www.forbes.ru/biznes/?page='
urls = []
for i in range(1, 21):
  new_url = url + str(i)
  urls.append(new_url)

news_titles = []
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('p', class_="XjpMy")
        for title in titles:
            span_title = title.find('span')
            if span_title and span_title.text not in news_titles:
                news_titles.append(span_title.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    time.sleep(1)

"""Страницы 21 - 50"""

url = 'https://www.forbes.ru/biznes/?page='
urls1 = []
for i in range(21, 51):
  new_url = url + str(i)
  urls1.append(new_url)

news_titles1 = []
for url in urls1:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('p', class_="XjpMy")
        for title in titles:
            span_title = title.find('span')
            if span_title and span_title.text not in news_titles1:
                news_titles1.append(span_title.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    time.sleep(10)

"""Страницы 51 - 80"""

url = 'https://www.forbes.ru/biznes/?page='
urls2 = []
for i in range(51, 81):
  new_url = url + str(i)
  urls2.append(new_url)

news_titles2 = []
for url in urls2:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('p', class_="XjpMy")
        for title in titles:
            span_title = title.find('span')
            if span_title and span_title.text not in news_titles2:
                news_titles2.append(span_title.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    time.sleep(10)

"""Страницы 81 - 120"""

url = 'https://www.forbes.ru/biznes/?page='
urls3 = []
for i in range(81, 121):
  new_url = url + str(i)
  urls3.append(new_url)

news_titles3 = []
for url in urls3:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('p', class_="XjpMy")
        for title in titles:
            span_title = title.find('span')
            if span_title and span_title.text not in news_titles3:
                news_titles3.append(span_title.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    time.sleep(10)

"""Страницы 121 - 200"""

url = 'https://www.forbes.ru/biznes/?page='
urls4 = []
for i in range(121, 200):
  new_url = url + str(i)
  urls4.append(new_url)

news_titles4 = []
for url in urls4:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('p', class_="XjpMy")
        for title in titles:
            span_title = title.find('span')
            if span_title and span_title.text not in news_titles4:
                news_titles4.append(span_title.text)
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {url}: {e}")
    time.sleep(10)

print(news_titles4)
print(len(news_titles4))

with open('Forbes', 'a', encoding='utf-8') as file:
    for title in news_titles4:
        file.write(title + '\n')

"""# Starhit (общество) - 2083"""

url = 'https://www.starhit.ru/life/page-'
urls = []
for i in range(1, 100):
  new_url = url + str(i) + '/'
  urls.append(new_url)

news_titles = []
for url in urls:
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  titles = soup.find_all('span', class_="announce-text-under-image__title ma-0")
  for title in titles:
    title = title.find(class_="announce-text-under-image__title-text")
    if title.text not in news_titles:
      news_titles.append(title.text)

with open('Starhit', 'w', encoding='utf-8') as file:
    for title in news_titles:
        file.write(title + '\n')