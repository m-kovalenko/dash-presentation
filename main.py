from datetime import date, datetime

import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/m-kovalenko/dash-presentation/main/beautiful_data.csv')
df.datetime = df.datetime.apply(datetime.fromisoformat)


app.layout = html.Div(children=[
    html.H1(children='Beautiful DASHboard'),
    dcc.DatePickerSingle(
        id='beautiful-date-picker',
        min_date_allowed=date(2022, 11, 6),
        max_date_allowed=date(2022, 11, 16),
        initial_visible_month=date(2022, 11, 16),
        date=date(2022, 11, 16)
    ),
    dcc.Graph(
        id='beautiful-graph',
        figure=px.line(pd.DataFrame())
    )
])


@app.callback(
    Output(component_id='beautiful-graph', component_property='figure'),
    Input(component_id='beautiful-date-picker', component_property='date')
)
def update_beautiful_graph(input_date):
    initial_state_df = df.loc[df.datetime.dt.date.astype(str) == input_date]
    fig = px.line(initial_state_df, x="datetime", y="value")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
