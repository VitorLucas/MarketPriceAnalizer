from Integrations.IntegrationsBuilder import integrations
from Repository.DataBase import MarketDataBase
from Helpers.LoggerHandler import logging
from Helpers.Configurations import config, product_list

items_to_find = product_list["name"]

if __name__ == "__main__":
    logging.info(f'Enviroment.{config["environment"]}')
    logging.info('Start search for products.')

    MarketDataBase.create_table()

    match config["state"]:
        case "DATA_COLLECT":
            logging.info('State of data collection activated.')
            for i in range(0, len(product_list)):
                for j in range(0, len(items_to_find)):
                    logging.info(f'Start search for products in {integrations[i].name} market')
                    MarketDataBase.add_products(integrations[i].find(items_to_find[j]))

        case "DATA_ANALIZE":
            NotImplemented
        case _:
            logging.info('No state was set in configuration.json file.')

    logging.info(f'Finish search and store products.')