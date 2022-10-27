from Integrations.IntegrationBuilder import integrations
from Repository.DataBase import MarketDataBase
from Helpers.LoggerHandler import logging
from Helpers.Configuration import config, product_list

items_to_find = product_list["name"]

if __name__ == "__main__":
    logging.info(f'Enviroment.{config["environment"]}')
    logging.info('Start search for products.')

    MarketDataBase.create_table()

    for i in range(0, len(product_list)):
        for j in range(0, len(items_to_find)):
            logging.info(f'Start search for products in {integrations[i].name} market')
            MarketDataBase.add_products(integrations[i].find(items_to_find[j]))

    logging.info(f'Finish search and store products.')