import panel as pn
import altair as alt
import pandas as pd
import sqlite3 as sql
import datetime as dt

from Repository.DataBase import MarketDataBase


class Plot():
    global tickerCompany
    global tickerFruit
    global date_range_slider
    global source
    title =''

    def update_fruits(which_seller):
        conn = MarketDataBase.get_connection()
        cursor = conn.cursor()

        cursor.execute(f"select distinct iif(seller == 'Continente', coalesce(product,'') || ' ' || coalesce(quantity,"
                       f"''),product) product from PRODUCTS where seller = '{which_seller}' order by product")
        return [i[0] for i in cursor.fetchall()]  # convert to list


    def company_changed(self,*event):
        global fruits, tickerFruit
        fruits = update_fruits(event[0].new)
        tickerFruit.options = fruits


    def get_plot(self,ticker_company, ticker_fruit, date_range):
        # Load and format the data
        conn = MarketDataBase.get_connection()
        source = pd.read_sql(
            "SELECT strftime('%d-%m-%Y', datetime(occurrence/1000, 'unixepoch', 'localtime')) as date,price,seller,"
            "iif(seller == 'Continente', coalesce(product,'') || ' ' || coalesce(quantity,''),product) product  from PRODUCTS",
            conn)
        df = source
        df['date'] = pd.to_datetime(df['date'], dayfirst=True)  # format date as datetime

        # create a date filter that uses values from the date range slider
        start_date = date_range_slider.value[0]  # store the first date range slider value in a var
        end_date = date_range_slider.value[1]  # store the end date in a var
        mask = (df['date'] > start_date) & (df['date'] <= end_date)  # create filter mask for the dataframe
        df = df.loc[mask]  # filter the dataframe
        df = df.loc[df['seller'] == ticker_company]  # filter the dataframe
        df = df.loc[df['product'] == ticker_fruit]  # filter the dataframe

        print(df.head())
        chart = alt.Chart(df) \
            .mark_line(point=True, color="red", opacity=0.8) \
            .encode(x='date', y='price', tooltip=alt.Tooltip(['date', 'price']))
        return chart


    def chart(self):
        self.get_plot()
        dashboard = pn.template.BootstrapTemplate(title=title)
        return dashboard.sidebar.append(pn.Column("#Options",
                                           date_range_slider,
                                           tickerCompany,
                                           tickerFruit,
                                           css_classes=['panel-widget-box']))

    pn.extension(sizing_mode='stretch_width')

    css = '''
      .bk.panel-widget-box {
        background: #f0f0f0;
        border-radius: 5px;
        border: 1px black solid;
        min-height: 330px;
      }
      '''

    pn.extension(raw_css=[css])

    conn = MarketDataBase.get_connection()
    cursor = conn.cursor()

    date_range_slider = pn.widgets.DateRangeSlider(
        name='Date Range Slider',
        start=dt.datetime(2022, 1, 1), end=dt.datetime(2023, 12, 31),
        value=(dt.datetime(2022, 1, 1), dt.datetime(2023, 12, 31))
    )

    title = '## Evolution of fruit prices'
    cursor.execute("select distinct seller from PRODUCTS order by product")

    sellers = [i[0] for i in cursor.fetchall()]  # convert to list
    tickerCompany = pn.widgets.Select(name='Seller', options=sellers)
    fruits = update_fruits(sellers[0])
    tickerFruit = pn.widgets.Select(name='Fruit', options=fruits)

    title = 'Market analysis:'
    tickerCompany = pn.widgets.Select(name='Seller', options=sellers)
    tickerFruit = pn.widgets.Select(name='Fruit', options=fruits)
    tickerCompany.param.watch(company_changed, 'value')