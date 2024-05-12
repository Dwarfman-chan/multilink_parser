# import requests
# from bs4 import BeautifulSoup


# def get_text_and_links(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             text = soup.get_text()
#             links = [link.get('href') for link in soup.find_all('a')]
#             return text, links
#         else:
#             print(f"Ошибка при запросе к {url}: {response.status_code}")
#             return None, None
#     except Exception as e:
#         print(f"Произошла ошибка: {str(e)}")
#         return None, None

# urls = [
#     'https://www.youtube.com/watch?v=qOSZMnCwums',
#     'https://e-zoo.com.ua/',
# ]

# for url in urls:
#     print(f"Анализируем страницу: {url}")
#     text, links = get_text_and_links(url)
#     if text and links:
#         print(f"{text}")
#         print()
#         print(f"{links}")


import asyncio
import aiohttp
import aiofiles
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from aiohttp.client_exceptions import InvalidURL

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except aiohttp.ClientConnectorError as e:
        print(f"Ошибка подключения: {e}")
        return ''

async def get_links(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        soup = BeautifulSoup(html, 'html.parser')
        links = [link.get('href') for link in soup.find_all('a')]
        wrong_links = ['/', '', None, '#']
        links = [link for link in links if link not in wrong_links]

        page_text = soup.get_text()
        page_text = page_text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')

        return links, page_text

async def scrape_page(url, file, base_link):
    async with aiohttp.ClientSession() as session:
        try:
            async with aiohttp.ClientSession() as session:
                if not url.startswith('http') or not url.startswith('https'):
                    url = urljoin(base_link, url)
                html = await fetch(session, url)
                soup = BeautifulSoup(html, 'html.parser')
                text = soup.get_text()
                text = text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
                async with aiofiles.open(file, 'a', encoding='utf-8', errors='replace') as f:
                    await f.write(text)
        except (InvalidURL, AssertionError) as e:
            print(f"Ошибка подключения: {e}")
        

async def main():
    urls = [
        'https://www.youtube.com/watch?v=qOSZMnCwums',
        'https://e-zoo.com.ua/',
        'https://art-lemon.com/portfolio',

    ]
    for base_link in urls:
        domain_name = urlparse(base_link).hostname
        links, page_text = await get_links(base_link)

        async with aiofiles.open(f'{domain_name}.txt', 'a', encoding='utf-8', errors='replace') as f:
            await f.write(page_text)
        await asyncio.gather(*[scrape_page(link, f'{domain_name}.txt', base_link) for link in links])


if __name__ == "__main__":
    asyncio.run(main())

"https://www.youtube.com/t/privacy"
'https://e-zoo.com.ua#v-pills-3-best'