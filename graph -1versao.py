import matplotlib.pyplot as plt
from datetime import datetime


def criaGraficoEgeon(dados):

    nome_arquivo = 'static/grafico_egeon.png'  # Nome do arquivo e local para salvar

    # Converter valores para datetime e int
    timestamps = [datetime.fromtimestamp(int(data[0])) for data in dados]
    values = [int(data[1]) for data in dados]

    # Plotagem do gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, values, marker='o', linestyle='-')

    # Configurações do gráfico
    plt.title('Gráfico Temporal')
    plt.xlabel('Tempo')
    plt.ylabel('Valores')
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(nome_arquivo)

    return nome_arquivo
