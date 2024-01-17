import plotly.graph_objs as go
from datetime import datetime, timedelta

def geraGrafico(dados, titulo, dias):
    # Converter os dados recebidos em timestamps
    timestamps = [datetime.fromtimestamp(int(data[0])) for data in dados]
    values = [int(data[1]) for data in dados]

    # Determinar a data inicial baseada no número de dias
    data_inicial = datetime.now() - timedelta(days=dias)

    # Filtrar os dados para manter apenas os últimos 'dias' dias
    timestamps_filtrados = []
    values_filtrados = []
    hover = [] 

    for i, timestamp in enumerate(timestamps):
        if timestamp >= data_inicial:
            timestamps_filtrados.append(timestamps[i])
            values_filtrados.append(values[i])
            hover.append(f'Data: {timestamps[i]}<br>Nodes: {values[i]}')

    trace = go.Scatter(
        x=timestamps_filtrados,
        y=values_filtrados,
        mode='lines',
        line=dict(color='green'),   
        hovertemplate='%{text}',
        name=''  
    )
    trace.text = hover

    data = [trace]

    layout = go.Layout(
        title=f'{titulo} - Gráfico Temporal dos últimos {dias} dias',
        xaxis=dict(title='Data / Hora'),
        yaxis=dict(title='Nodes'),        
        hovermode='closest',
    )

    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)
