from bs4 import BeautifulSoup as BS
import aiohttp
import asyncio
import lxml
import ssl
from fake_useragent import UserAgent
import requests
from pyshorteners import Shortener


HEADERS = {"User-Agent": UserAgent().random}

async def load_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=HEADERS, ssl=False) as response:
            r = await response.content.read()
            soup = BS(r, 'html.parser')
            items = soup.find_all('li', {'class': 'avatars__item'})
            shorteners = Shortener(timeout=5)
            for item in items:
                avatar = item.find('a', {'class': 'avatars__link'})
                link = avatar.get('href')
                img = request.get(url , stream =  True)
                name = url.split('/')[-1]
                file = open('PICTURES/{name}','bw')
                for chunk in img.iter_content(4095):
                    file.write(chunk)
                    
            
async def main():
    images = []
    shorteners = Shortener(timeout=4)
    for i in range(1, 200):
        url = f"https://cspromogame.ru/avatars?page={i}"
        try:
            await load_data(url)
        except Exeption as e:
            print('you have an error')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



