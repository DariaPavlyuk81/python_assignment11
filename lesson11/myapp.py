import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#  gapminder dataset
df = px.data.gapminder()

# sorted list of countries
countries = sorted(df['country'].unique())

#  Dash app
app = dash.Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    html.H1("GDP per Capita Growth by Country", style={'textAlign': 'center'}),
    
    html.Label("Select a Country:"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  
    ),
    
    dcc.Graph(id='gdp-growth')
])


@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    filtered_df = df[df['country'] == selected_country]
    
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f"GDP Per Capita Growth: {selected_country}",
        markers=True
    )
    fig.update_layout(template='plotly_dark')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
