import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'color': '#b1f2c2',
    'text': '#4287f5',
    'background': 'yellow'
}
app.layout = html.Div([
    html.H2('Hello Dash',
            style={'color': colors['text'],
                   'textAlign': 'center'}),
    html.Div('a web framework',
             style={'color': colors['text'],
                    'textAlign': 'center'}),
    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x=[2017, 2018, 2019],
                y=[210, 100, 3000],
                marker_color='pink',
                marker_line_color='black',
                marker_line_width=5,
                name='lokalnie'
            ),
            go.Bar(
                x=[2017, 2018, 2019],
                y=[220, 200, 2000],
                marker_color='pink',
                marker_line_color='black',
                marker_line_width=5,
                name='online'

            )],
            layout=go.Layout(title='wizualizacja danych',
                             plot_bgcolor=colors['background'],
                             paper_bgcolor='orange'
                             )

        ))

], style={'backgroundColor' : colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)
