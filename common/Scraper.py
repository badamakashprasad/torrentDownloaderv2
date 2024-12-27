import requests
import os
from urllib.parse import urljoin
from dotenv import load_dotenv
from typing import Dict, List, Optional

class Scraper:
    def __init__(self, site: str) -> None:
        load_dotenv()
        self.base_url = os.getenv(site.upper())
        assert self.base_url, f"Environment variable for {site.upper()} is not set"   

    def getBaseUrl(self) -> str:
        return self.base_url

    def getCategories(self, categoryDict: Dict[str, List[str]]) -> List[str]:
        categories: Dict = []
        assert categoryDict, "Category dictionary is empty"
        if "categories" in categoryDict:
            categories = categoryDict["categories"]
        return categories

    def getEndpoint(self, endpointDict: Dict[str, any], category: str) -> str:
        endpoint: str = ""
        assert endpointDict, "Endpoint dictionary is empty"
        assert category, "Category is empty"
        if "prefix" in endpointDict:
            endpoint = endpointDict["prefix"] + endpointDict["delimiter"] + category
        if "suffix" in endpointDict:
            if "delimiter" in endpointDict:
                endpoint = endpoint + endpointDict["delimiter"] + endpointDict["suffix"]
            else:
                endpoint = endpoint + endpointDict["suffix"]
        return endpoint

    def get_page(self, endpoint: str) -> Optional[str]:
        url = urljoin(self.base_url, endpoint)
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_pages(self, endpoints: List[str]) -> Dict[str, Optional[str]]:
        pages = {}
        for endpoint in endpoints:
            pages[endpoint] = self.get_page(endpoint)
        return pages