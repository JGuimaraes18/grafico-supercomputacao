import plotly.graph_objs as go
from datetime import datetime


def geraGrafico(dados, titulo):
    timestamps = [datetime.fromtimestamp(int(data[0])) for data in dados]
    values = [int(data[1]) for data in dados]

    trace = go.Scatter(x=timestamps, y=values, mode='lines', line=dict(color='green') )
    data = [trace]

    layout = go.Layout(
        title=titulo,
        xaxis=dict(title='Data'),
        yaxis=dict(title='Nodes'),
        hovermode='closest',
    )

    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)
