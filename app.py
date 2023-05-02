import dash
from dash import html


app = dash.Dash('app')

app.layout = html.Div(["Hello World"])
if __name__ == '__main__':
    app.run_server(port=5000)