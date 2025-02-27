import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px


dash.register_page(__name__)

layout = html.Div([
    html.H2('Interactive Charts'),
    html.Div('... Interactive Charts'),
])