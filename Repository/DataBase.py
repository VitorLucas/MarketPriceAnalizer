import sqlite3 as sql
from Helpers.Configurations import config
from Helpers.LoggerHandler import logging

class MarketDataBase:

    def get_connection():
        if(config["environment"] == "Development"):
            logging.info('Connection to productsDev.db')
            conn = sql.connect('productsDev.db')
        else:
            logging.info('Connection to products.db')
            conn = sql.connect('products.db')

        return conn

    @classmethod
    def create_table(self):
        conn = self.get_connection()
        cur = conn.cursor()

        logging.info(f'Creating table Products')
        query = """ CREATE TABLE  if not exists  PRODUCTS (
                        seller VARCHAR(50),
                        occurrence INTEGER,
                        product VARCHAR(100),
                        price REAL,
                        quantity VARCHAR(100)
                        );"""

        try:
            cur.execute(query)
            conn.commit()
            conn.close()
        except NameError:
            logging.error(F'error while create table PRODUCTS: {NameError}')

    @classmethod
    def add_products(self, products):
        conn = self.get_connection()
        cur = conn.cursor()

        logging.info(f'Adding products count: {len(products)}')

        query ="INSERT INTO PRODUCTS(seller,occurrence,product,price,quantity) VALUES(?,?,?,?,?)"
        for item in products:
            cur.execute(query, (item.seller, item.occurrence, item.product, item.price, item.quantity))

        try:
            conn.commit()
            conn.close()
            logging.info('Finished add')
        except NameError:
            logging.error(f'error while add products: {NameError}')

    @classmethod
    def get_products(self):
        conn = self.get_connection()
        cur = conn.cursor()
        query = "SELECT seller, strftime('%d', datetime(occurrence/1000, 'unixepoch', 'localtime')) AS day, product, CAST(price as decimal)price FROM PRODUCTS"
        cur.execute(query)
        products = cur.fetchall()

        return products