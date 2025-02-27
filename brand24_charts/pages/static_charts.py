import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

dash.register_page(__name__)

# WPS Data from 30/09/2024 to 23/02/2025
df = pd.read_csv('https://raw.githubusercontent.com/JuanBatnag/plotly_pandas_practice/refs/heads/main/ALL_WPS_2025-02-24_03.18.csv')
# Sort data by date descending 
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True).dt.date
df.sort_values(by=['Date'], inplace=True)

layout = html.Div([
    html.H2('Static Charts'),
    html.Hr(),
    html.H3('Select Timeframe'),
    dcc.RadioItems(
        id='timeframe_selector',
        options=['Today', 'Yesterday', 'Last 7 days', 
                 'Last Thirty Days', 'Last Year', 'All'],
        value='All'),
    # Mentions per day graph:
    dcc.Graph(figure={}, id='mentions_per_day')
])

@callback(
    Output('mentions_per_day', 'figure'),
    [Input('timeframe_selector', 'value')]
)

def update_mentions_graph(timeframe):
    # Assumes that dataframe is up to date.
    # Will not show any data for "Today" if there was no data scraped for that day.

    if timeframe:
        # Match user input with datetime.date object
        match timeframe:
            case 'Today':
                selected_date = date.today()
            case 'Yesterday':
                selected_date = date.today() - timedelta(days=1)
            case 'Last 7 days':
                selected_date = date.today() - timedelta(days=7)
            case 'Last Thirty Days':
                selected_date = date.today() - timedelta(days=30)
            case 'Last Thirty Days':
                selected_date = date.today() - relativedelta(months=3)
            case 'Last Year':
                selected_date = date.today() - relativedelta(years=1)
            case 'All':
                selected_date = date(2024, 9, 30) # Start of dataset

        # Graphing mentions:
        df_to_date = df[df['Date'] >= selected_date]
        mentions_per_day = df_to_date.groupby('Date').size().reset_index(name='Mentions_Count')
        mentions_graph = px.area(mentions_per_day, x='Date', y='Mentions_Count')
        mentions_graph.update_layout(plot_bgcolor='white')

        return mentions_graph

    else:
        return print('No timeframe selected')
        