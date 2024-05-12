import asyncio
import aiohttp
import aiofiles
import json
import re
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

        page_text = soup.get_text(separator=' ')
        page_text = page_text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
        page_text = re.sub(r'\s+', ' ', page_text)

        return links, page_text


async def main():
    urls = [
        'https://www.youtube.com/watch?v=qOSZMnCwums',
        'https://e-zoo.com.ua/',
        'https://art-lemon.com/portfolio',
    ]
    
    for base_link in urls:
        domain_name = urlparse(base_link).hostname
        links, page_text = await get_links(base_link)
        data_json = {'links': links, 'mainPageText': page_text, 'baseURL': base_link}

        # async with aiofiles.open(f'data{domain_name}.json', 'w', encoding='utf-8') as f:
        #     await f.write(page_text)
        async with aiofiles.open(f'data/{domain_name}.json', 'w', encoding='utf-8') as f:
            await f.write(json.dumps(data_json, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    asyncio.run(main())

