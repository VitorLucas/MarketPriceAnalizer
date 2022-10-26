import sqlite3 as sql
from Helpers.Configuration import config

class MarketDataBase:

    def get_connection():
        if(config["environment"] == "Development"):
            conn = sql.connect('productsDev.db')
        else:
            conn = sql.connect('products.db')
        return conn

    @classmethod
    def create_table(self):
        conn = self.get_connection()
        cur = conn.cursor()

        query = """ CREATE TABLE  if not exists  PRODUCTS (
                        seller VARCHAR(50),
                        occurrence INTEGER,
                        product VARCHAR(100),
                        price REAL,
                        quantity VARCHAR(100)
                        );"""

        cur.execute(query)
        conn.commit()

    @classmethod
    def add_products(self, products):
        conn = self.get_connection()
        cur = conn.cursor()

        query ="INSERT INTO PRODUCTS(seller,occurrence,product,price,quantity) VALUES(?,?,?,?,?)"
        for item in products:
            cur.execute(query, (item.seller, item.occurrence, item.product, item.price, item.quantity))

        conn.commit()
        conn.close()