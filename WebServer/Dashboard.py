import dash
from dash import html
from dash import dcc
from dash.dash_table import DataTable
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from Repository.DataBase import MarketDataBase

products = MarketDataBase.get_products()

days = []
price = []
for i in range(0, len(products)):
    price.append(products[i][3])
    days.append(products[i][1])

title_font_size = 30
figure_daily_sales_number = px.line(x=days, y=price,title="Daily number of sales",width=800,height=800).update_layout(title_font_size=title_font_size)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        html.H1("Sales KPIs"),
        html.H2("Sales Dataset"),
        dcc.Graph(figure=figure_daily_sales_number)
    ]
)