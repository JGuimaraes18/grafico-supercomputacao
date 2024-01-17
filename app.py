from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
from connection import *
from graph import *

app = Flask(__name__)
app.secret_key = 'Inpe2023'

@app.route('/', methods=['GET', 'POST'])
def index():
    db = get_db()
    cursor = db.cursor()
    egeon = buscaDadosEgeon(cursor)
    xc50 = buscaDadosXC50(cursor)

    graficoEgeon = geraGrafico(egeon, 'Egeon', 30)
    graficoXC50 = geraGrafico(xc50, 'XC50', 30)

    return render_template('dados.html', dados=egeon, graficoEgeon=graficoEgeon, graficoXC50=graficoXC50)

@app.route('/atualizar-grafico', methods=['GET'])
def atualizar_grafico():
    db = get_db()
    cursor = db.cursor()
    dias = int(request.args.get('dias', 7))
    egeon = buscaDadosEgeon(cursor)
    graficoEgeon = geraGrafico(egeon, 'Egeon', dias)

    return graficoEgeon



if __name__ == '__main__':
    # Production
    http_server = WSGIServer(('', 5003), app)
    http_server.serve_forever()
