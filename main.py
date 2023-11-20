from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go
import pandas as pd



app = Dash(__name__)
app.server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

df = pd.read_csv('Group4.csv', low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])
unique_dec_code = df['DEC_code'].unique()

app.layout = html.Div([
    html.H4('Apple stock candlestick chart'),

    dcc.Dropdown(
        className="dropdown",
        id='dec-code-filter',
        options=unique_dec_code,
        value='DEC10M10'
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("dec-code-filter", "value"))
def display_candlestick(value):
    filtered_df = df[df['DEC_code']== value]
    fig = go.Figure(go.Candlestick(
        x=filtered_df['Date'],
        open=filtered_df['Open'],
        high=filtered_df['High'],
        low=filtered_df['Low'],
        close=filtered_df['Close']
    ))

    fig.update_layout(xaxis_rangeslider_visible=False)

    fig.update_layout(
    xaxis=dict(
        showline=True,
        showgrid=False,
        showticklabels=True,
        #linecolor='rgb(204, 204, 204)',
        linewidth=1,
        ticks='outside',
        tickfont=dict(
            family='Arial',
            size=12,
            color='rgb(82, 82, 82)')))

    # Change background color to white
    fig.update_layout(plot_bgcolor='white')
    fig.update_xaxes(showline=True, linewidth=0.5, linecolor='gray', showticklabels=True)
    fig.update_yaxes(showline=True, linewidth=0.5, linecolor='gray')

    return fig




if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
