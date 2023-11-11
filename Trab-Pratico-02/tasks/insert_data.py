import psycopg2
from psycopg2 import sql

def insert_navios(conn, navios_dict):
    cursor = conn.cursor()
    for key, item in navios_dict.items():
        nome = item['nome']
        tipo = item['tipo']
        cursor.execute("INSERT INTO Embarcacoes (nome, tipo) VALUES (%s, %s)", (nome, tipo))
        print("Navio adicionado com sucesso:", item)
    conn.commit()
    cursor.close()

def insert_tripulantes(conn, tripulantes_dict):
    cursor = conn.cursor()
    for key, item in tripulantes_dict.items():
        nome = item['nome']
        data_nasc = item['data_nasc']
        funcao = item['funcao']
        id_emb = item['id_emb']
        cursor.execute("INSERT INTO Tripulantes (nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", (nome, data_nasc, funcao, id_emb))
        print("Tripulante adicionado com sucesso:", item)
    conn.commit()
    cursor.close()

def insert_empregados(conn, empregados_dict):
    cursor = conn.cursor()
    for key, item in empregados_dict.items():
        nome = item['nome']
        data_nasc = item['data_nasc']
        funcao = item['funcao']
        cursor.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", (nome, data_nasc, funcao))
        print("Empregado adicionado com sucesso:", item)
    conn.commit()
    cursor.close()
    