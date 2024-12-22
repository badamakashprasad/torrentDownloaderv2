import requests
from urllib.parse import urljoin,urlencode,urlparse
from dotenv import load_dotenv
import os

#data = requests.get("https://eztv.tf/api/get-torrents?limit=100&page=1")

load_dotenv()


class Params:
    _instance = None
    limit = 100
    page = 1
    total = None
    totalPages = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def setLimit(self,limit):
        assert limit >= 1 and limit <= 100 , "limit per page should be between 1 and 100"
        self.limit = limit
    

    def setPage(self,page):
        assert self.totalPages != None  , "Total Pages is None"
        assert self.page < self.totalPages , "page no is greater than total pages"
        self.page = page
      
    
    def setTotal(self,total):
        assert total > 0 , "total cannot be less than zero"
        self.total = total
        self.setTotalPages()

    def setTotalPages(self):
        assert self.total != None , "total is None"
        self.totalPages = self.total // self.limit if self.total % self.limit == 0 else (self.total // self.limit) + 1

    def getParams(self):
        if self.total != None:
            self.totalPages = self.total // self.limit if self.total % self.limit == 0 else (self.total // self.limit) + 1
        return {
            "limit" : self.limit,
            "page" : self.page
        }
      

class EzTv:
    params = Params()
    base_url = os.getenv("BASE_URL")
    data = None

    def getUrl(self):
        return urljoin(self.base_url,"api/get-torrents")

    def getResponse(self):
        url = self.getUrl()
        response = requests.get(url,self.params.getParams())
        print(response.status_code)
        if response.status_code == 200:
            self.data = response.json()
        try:
            self.params.setTotal(self.getTotalTorrents())
            self.params.setPage(self.params.page + 1)
        except AssertionError:
            print("Error occured in setting auto params")
        return self.data
    
    def getTorrents(self):
        if self.data == None:
            self.getResponse()
        return self.data["torrents"]

    def getTotalTorrents(self):
        if self.data == None:
            self.getResponse()
        return int(self.data["torrents_count"])



if __name__ == '__main__':
    eztv = EzTv()
    data = eztv.getResponse()
    eztv = EzTv()
    data2 = eztv.getResponse()
    print(data)
    print(data2)



