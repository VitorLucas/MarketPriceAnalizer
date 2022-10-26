import requests
from bs4 import BeautifulSoup

class IntegrationBase:
    @classmethod
    def extract_dom(self, market_url, iten_to_search):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'}
        url = market_url + iten_to_search
        r = requests.get(url, headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup