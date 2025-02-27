import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd

dash.register_page(__name__, path='/')

# WPS Data from 30/09/2024 to 23/02/2025
df = pd.read_csv('https://raw.githubusercontent.com/JuanBatnag/plotly_pandas_practice/refs/heads/main/ALL_WPS_2025-02-24_03.18.csv')
# Sort data by date descending 
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df.sort_values(by=['Date'], inplace=True)

layout = html.Div([
    html.H2('West Philippine Sea Data'),
    html.Hr(),
    # Datatable for reference
    dash_table.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_cell={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': 0,
        },
        tooltip_data=[
            {
                column: {'value': str(value), 'type': 'markdown'}
                for column, value in row.items()
            } for row in df.to_dict('records')
        ],
        tooltip_duration=None
    )
])
