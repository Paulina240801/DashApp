import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.Label('wybierz preferowany jezyk'),
    dcc.Dropdown(
        options=[
            {'label':'Python', 'value':'py'},
            {'label':'SQL', 'value':'sql'},
            {'label':'JavaScript', 'value':'js'}
        ]
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        value='py',
        multi=True,
        searchable=False
    ),
dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        placeholder='wybierz technologie'
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
