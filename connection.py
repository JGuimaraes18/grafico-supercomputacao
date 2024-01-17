import os
import pymysql.cursors
from flask import Flask, g
from dotenv import load_dotenv


app = Flask(__name__)   

# Carrega as variaveis do env para comunicação com BD #
load_dotenv()

def get_db():
    if 'db' not in g:
        # Conectando ao banco de dados
        g.db = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=os.getenv('DB_NAME')
        )
    return g.db

def buscaDadosEgeon(cursor):
    cursor.execute('SELECT `update`, running FROM history_super_egeon;')
    resultSearch = cursor.fetchall()
    return resultSearch

def buscaDadosXC50(cursor):
    cursor.execute('SELECT `update`, running FROM history_super_xc50;')
    resultSearch = cursor.fetchall()
    return resultSearch