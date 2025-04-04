import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

def conectar():
    try:
        connectionString = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={os.getenv("SQL_SERVER")};'
            f'DATABASE={os.getenv("SQL_DATABASE")};'
            f'UID={os.getenv("SQL_USERNAME")};'
            f'PWD={os.getenv("SQL_PASSWORD")}'
        )

        conn = pyodbc.connect(connectionString)
        # print('Conectou')
        return conn
    except Exception as erro:
        print('Erro ao conectar -->', erro)

def desconectar(conn):
    conn.close()
    # print("Desconectado")


def query(query):
    conn = conectar()
    cursor = conn.cursor()
    try:
    #strip() remove espaços no inicio e fim da string
    #upper() auto explicativo =)
    #startswith() Verifica se a string começa com...
        if query.strip().upper().startswith("SELECT"): #aqui eu dei uma roubada para pensar em como fazer para select fazer algo e insert, update e delete fazer outra
            try:
                cursor = conn.cursor()
                cursor.execute(query)
                resultado = cursor.fetchall()
                return resultado
            except Exception as erro:
                print("Erro no select -->", erro)
                return []     
        cursor.execute(query)
        conn.commit()
        print("Sucesso na query -->")
    except Exception as erro:
        print(f"Erro na query --> '{erro}'")
    finally:
        desconectar(conn)

