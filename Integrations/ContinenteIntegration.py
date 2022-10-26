from Integrations.IntegrationBase import IntegrationBase
from Models.Product import Product
from Helpers.TimeZone import TimeZone
from Helpers.Configuration import config

class ContinenteIntegration(IntegrationBase):

    @classmethod
    def find(self, iten_to_search):
        url = config["continente"]["url"]
        joblist = []
        soup = self.extract_dom(url, iten_to_search)
        divs = soup.find_all('div', {'class': 'ct-tile-body col col-sm-auto'})
        company='Continente'

        for item in divs:
            title = item.find('a').text.strip()

            if title.upper().startswith(iten_to_search.upper()):
                producer = item.find('p', {'class': 'ct-tile--brand'}).text.strip()
                try:
                    price = float(item.find('span', {'class': 'value'})['content'].strip())
                except:
                    price = ''

                quantity = item.find('p', {'class': 'ct-tile--quantity'}).text.strip()
                joblist.append(Product(company, TimeZone.generate_timeZone(), title, price, quantity))

        return joblist