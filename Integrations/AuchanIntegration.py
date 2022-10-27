from Repository.Models.Product import Product
from Integrations.IntegrationBase import IntegrationBase
from Helpers.TimeZone import TimeZone
from Helpers.Configurations import config
from Helpers.LoggerHandler import logging

class AuchanIntegration(IntegrationBase):

    name = config["auchan"]["market"]
    @classmethod
    def find(self, iten_to_search):
        url = config["auchan"]["url"]

        joblist = []
        try:
            soup = self.extract_dom(url, iten_to_search)
            divs = soup.find_all('div', {'class': 'auc-product'})
            company = 'Auchan'

            for item in divs:
                title = item.find('a', {'class': 'link'}).text.strip()

                if title.upper().startswith(iten_to_search.upper()):
                    try:
                        price = float(item.find('span', {'class': 'value'})['content'].strip())
                    except:
                        price = ''

                    joblist.append(Product(company, TimeZone.generate_timeZone(), title, price, ""))

            return joblist
        except:
            logging.error(f'Error while try to scrap the market: {name}')