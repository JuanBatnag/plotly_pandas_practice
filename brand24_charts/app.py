import dash
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Initialize the app
app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1('Brand 24 Interactive Charts'),
    html.Div([
        html.Div(
            dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
        ) for page in dash.page_registry.values()
    ]),
    dash.page_container
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)