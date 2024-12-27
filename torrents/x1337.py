from typing import Dict, List, Optional
from common.Scraper import Scraper
from common.Constant import ScraperEndpoints
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from pyjsparser import parse
import json

class x1337:
    def __init__(self):
        self.site = "X1337"
        self.scrapper = Scraper(self.site)
        self.base_url = self.scrapper.getBaseUrl()
        self.params = ScraperEndpoints().x1337
        self.categories = self.scrapper.getCategories(self.params)
        pass
    

    def getTrendingPages(self,type : Optional[str]) -> any:
        if type and type in self.categories:
            endpoint = self.scrapper.getEndpoint(self.params,type)
            return self.scrapper.get_page(endpoint)
        else:
            pages: Dict = {}
            for type in self.categories:
                endpoint = self.scrapper.getEndpoint(self.params,type)
                pages[type] = self.scrapper.get_page(endpoint)
            return pages
        
    def retrieveTorrentUrls(self,page: Optional[str]) -> List[str]:
        ret = []
        if page:     
            soup = BeautifulSoup(page, 'html.parser')
            table = soup.find('div', class_='featured-list').select_one('table')
            hrefs = [td.select('a')[1].get('href') for td in table.find_all('td', class_='coll-1 name')]
            urls = [urljoin(self.base_url,href) for href in hrefs]
        return urls

    def getBeautifulSoup(self,url: Optional[str]) -> any:
        page = self.scrapper.get_page(url)
        if page:
            return BeautifulSoup(page, 'html.parser')
        return None

    def getTorrentData(self,soup: Optional[any]) -> Dict[str, any]:
        data = {}
        if soup:
            for ul in soup.find_all('ul', class_='list')[1:]:
                for li in ul.find_all('li'):
                    data[li.find('strong').text] = li.find('span').text
            script = soup.find_all('script',type="text/javascript")[1]
            parsed = parse(script.text)
            data["magnet"] = parsed['body'][0]['declarations'][0]['init']['value']
        return data

