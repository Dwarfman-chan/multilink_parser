import os
import json
import asyncio
import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

async def deeplink_scraper(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

        base_link = data.get('baseURL')
        main_page = data.get('mainPageText')
        links = data.get('links')

        deeplink_text = [{'url': base_link, 'site_text': main_page},]

        # удалить ограничение или выставить требуемое
        for link in links[0:50]:
            if not link.startswith('http') or not link.startswith('https'):
                link = urljoin(base_link, link)
            
            response = requests.get(link).text
            soup = BeautifulSoup(response, 'html.parser')

            page_text = soup.get_text(separator=' ')
            page_text = page_text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
            page_text = re.sub(r'\s+', ' ', page_text)

            deeplink_text.append({'url': link, 'site_text': page_text})
        
        # deeplink_text = [item for item in deeplink_text if 'Forbidden nginx' not in item.get('site_text')]

    domain_name = urlparse(base_link).hostname
    with open(f'deeplink_data/{domain_name}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(deeplink_text, ensure_ascii=False, indent=4))


async def main(dir_path, files):
    tasks = [deeplink_scraper(dir_path+file) for file in files]

    results = await asyncio.gather(*tasks)
    for result in results:
        if result:
            print(result)


if __name__ == "__main__":
    dir_path = 'data/'
    files = os.listdir(dir_path)

    asyncio.run(main(dir_path, files))

    # for file in files:
    #     with open(f'{dir_path}/{file}', 'r', encoding='utf-8') as file:
    #         data = json.load(file)
    #         print(data)