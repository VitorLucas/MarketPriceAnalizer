# -*- coding: utf-8 -*-
from Integrations.IntegrationsBuilder import integrations
from Repository.DataBase import MarketDataBase
from Helpers.LoggerHandler import logging
from Helpers.Configurations import config, product_list
from Helpers.filter import Filter
#from WebServer.Dashboard import dashboard

items_to_find = product_list["name"]

if __name__ == "__main__":
    logging.info(f'Environment.{config["environment"]}')
    logging.info('Start search for products.')
    logging.info(Filter.filter_expression("teste"))
    MarketDataBase.create_table()

    match config["state"]:
        case "DATA_COLLECT":
            logging.info('State of data collection activated.')
            for i in range(0, len(product_list)):
                for j in range(0, len(items_to_find)):
                    logging.info(f'Start search for products in {integrations[i].name} market')
                    MarketDataBase.add_products(integrations[i].find(items_to_find[j]))

        case "DATA_ANALIZE":
            #test = MarketDataBase.get_products()
            #dashboard()

            print(Filter.filter_price(" 1.99 €/Kg"))
            print(Filter.filter_expression("Aperitivo Doritos Tex Mex 120g"))
        case _:
            logging.info('No state was set in configuration.json file.')

    logging.info(f'Finish search and store products.')