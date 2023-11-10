import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do banco e as atribui adequadamente
load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Conecta ao banco e cursor 
conn = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

cursor = conn.cursor()

navios = {
    1: ('Navio1', 'Cargueiro'),
    2: ('Navio2', 'Passageiro'),
    3: ('Navio3', 'Petroleiro'),
    4: ('Navio4', 'Cargueiro')
}

tripulantes = {
    1: {'nome': 'Tripulante1', 'data_nasc': '1990-01-15', 'funcao': 'Oficial de Convés', 'id_emb': 1},
    2: {'nome': 'Tripulante2', 'data_nasc': '1992-03-20', 'funcao': 'Engenheiro', 'id_emb': 1},
    3: {'nome': 'Tripulante3', 'data_nasc': '1988-11-05', 'funcao': 'Comissario de Bordo', 'id_emb': 2},
    4: {'nome': 'Tripulante4', 'data_nasc': '1995-06-30', 'funcao': 'Oficial de Convés', 'id_emb': 3},
    5: {'nome': 'Tripulante5', 'data_nasc': '1991-07-10', 'funcao': 'Capitão', 'id_emb': 4},
    6: {'nome': 'Tripulante6', 'data_nasc': '1994-09-25', 'funcao': 'Engenheiro', 'id_emb': 4}
    }

empregados = {
    1: {'nome': 'Employee1', 'data_nasc': '1985-05-12', 'funcao': 'Manutenção'},
    2: {'nome': 'Employee2', 'data_nasc': '1993-02-28', 'funcao': 'Segurança'},
    3: {'nome': 'Employee3', 'data_nasc': '1987-09-18', 'funcao': 'Logística'},
    4: {'nome': 'Employee4', 'data_nasc': '1990-12-05', 'funcao': 'Limpeza'},
    5: {'nome': 'Employee5', 'data_nasc': '2001-08-30', 'funcao': 'Manutenção'}
    }

movimentacoes = {
    1: {'data': '2023-09-01', 'tipo': 'Carga', 'id_emb': 1},
    2: {'data': '2023-09-02', 'tipo': 'Embarque de Passageiros', 'id_emb': 2},
    3: {'data': '2023-10-03', 'tipo': 'Abastecimento', 'id_emb': 3},
    4: {'data': '2023-10-05', 'tipo': 'Descarga', 'id_emb': 1},
    5: {'data': '2023-10-05', 'tipo': 'Manutenção', 'id_emb': 4}
    }

def insert_navios(navios_dict, cursor):
    for item, (nome,tipo) in navios_dict.items():
        cursor.execute("INSERT INTO Embarcacoes (nome, tipo) VALUES (%s, %s)", (nome, tipo))
        print("Navio adicionado com sucesso:", item)
    conn.commit()

def insert_tripulantes(tripulantes_dict, cursor):
    for key, item in tripulantes_dict.items():
        nome = item['nome']
        data_nasc = item['data_nasc']
        funcao = item['funcao']
        id_emb = item['id_emb']
        cursor.execute("INSERT INTO Tripulantes (nome, data_nasc, funcao, id_emb) VALUES (%s, %s, %s, %s)", (nome, data_nasc, funcao, id_emb))
        print("Tripulante adicionado com sucesso:", item)
    conn.commit()
def insert_empregados(empregados_dict, cursor):
    for key, item in empregados_dict.items():
        nome = item['nome']
        data_nasc = item['data_nasc']
        funcao = item['funcao']
        cursor.execute("INSERT INTO Empregados(nome, data_nasc, funcao) VALUES (%s, %s, %s)", (nome, data_nasc, funcao))
        print("Empregado adicionado com sucesso:", item)
    conn.commit()
    
insert_navios(navios, cursor)
insert_tripulantes(tripulantes, cursor)
insert_empregados(empregados, cursor)

conn.commit()
cursor.close()
conn.close()
    