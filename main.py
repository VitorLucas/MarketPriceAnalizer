from Integrations.ContinenteIntegration import ContinenteIntegration
from Integrations.AuchanIntegration import AuchanIntegration
from Repository.DataBase import MarketDataBase

if __name__ == "__main__":
    integragtions = [ContinenteIntegration, AuchanIntegration]
    items_to_find = ['Banana', 'Uva']

    #only to create database once
    #MarketDataBase.create_table()

    for i in range(0, len(integragtions)):
        for j in range(0, len(items_to_find)):
            MarketDataBase.add_products(integragtions[i].find(items_to_find[j]))