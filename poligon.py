import os
import json
import asyncio
import requests
import re
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from requests.exceptions import InvalidSchema, ConnectionError

HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Cookie': 'PHPSESSID=1ik4eonlrm3q370j0el9cq78j6; _gcl_au=1.1.1338874711.1715541993; _ga=GA1.2.1938333905.1715541993; _gid=GA1.2.100777519.1715541993; _fbp=fb.1.1715541993450.1273910433; _dc_gtm_UA-33040125-1=1; cf_clearance=l7Xj3hVdUcjv0M7aXBVlfuD80.PVfYZzgxg.HGCCSP4-1715551381-1.0.1.1-HoNANu.54fmkcAkxVTgrXqMIf9izng7SFIFd.eRbFzreN9kp1UaUgYrtXfABlTHUG_.8Iw348iSdhBKpJvlnuQ; biatv-cookie={%22firstVisitAt%22:1715541993%2C%22visitsCount%22:1%2C%22currentVisitStartedAt%22:1715541993%2C%22currentVisitLandingPage%22:%22https://art-lemon.com/portfolio%22%2C%22currentVisitUpdatedAt%22:1715551381%2C%22currentVisitOpenPages%22:3%2C%22campaignTime%22:1715551381%2C%22campaignCount%22:2%2C%22utmDataCurrent%22:{%22utm_source%22:%22google%22%2C%22utm_medium%22:%22organic%22%2C%22utm_campaign%22:%22(not%20set)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20provided)%22%2C%22beginning_at%22:1715551381}%2C%22utmDataFirst%22:{%22utm_source%22:%22google%22%2C%22utm_medium%22:%22organic%22%2C%22utm_campaign%22:%22(not%20set)%22%2C%22utm_content%22:%22(not%20set)%22%2C%22utm_term%22:%22(not%20provided)%22%2C%22beginning_at%22:1715541993}}; bingc-activity-data={%22numberOfImpressions%22:0%2C%22activeFormSinceLastDisplayed%22:414%2C%22pageviews%22:2%2C%22callWasMade%22:0%2C%22updatedAt%22:1715551396}',
    'Priority': 'u=0, i',
    'Referer': 'https://www.google.com/',
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def deeplink_scraper():
    link = '/ua/'
    base_link = 'https://art-lemon.com/ua/'
    if not link.startswith('http') or not link.startswith('https'):
        link = urljoin(base_link, link)
    
    response = requests.get(link, headers=HEADER).text
    print(response)
    # soup = BeautifulSoup(response, 'html.parser')

    # print(soup)

    # page_text = soup.get_text(separator=' ')
    # page_text = page_text.replace('\n', ' ').replace('\t', ' ').replace('\r', ' ')
    # page_text = re.sub(r'\s+', ' ', page_text)




deeplink_scraper()