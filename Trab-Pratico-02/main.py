import psycopg2
from psycopg2 import sql
import db_config
from tasks import create_tables, insert_data, queries, stored_procedure, transaction, triggers 
import setup

# Configura a conexão com base no .env
conn = db_config.db_conn()

# 2.1 Setup (apaga tudo do banco e reinicia)
setup.setup_tables(conn)

# 2.2 Cria as tabelas
create_tables.create_tables(conn)

# 2.3 Cria os dados
navios = {
    1: {'nome': 'Navio1', 'tipo':' Cargueiro'},
    2: {'nome': 'Navio2', 'tipo': 'Passageiro'},
    3: {'nome': 'Navio3', 'tipo': 'Petroleiro'},
    4: {'nome': 'Navio4', 'tipo': 'Cargueiro'}
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

movimentacoes_empregados = {
    1: {'id_mov': 1, 'id_emp': 1}, 
    2: {'id_mov': 1, 'id_emp': 3},
    3: {'id_mov': 2, 'id_emp': 2},
    4: {'id_mov': 3, 'id_emp': 1},
    5: {'id_mov': 3, 'id_emp': 4},
    6: {'id_mov': 4, 'id_emp': 1},
    7: {'id_mov': 4, 'id_emp': 3},
    8: {'id_mov': 5, 'id_emp': 1}
}

# 2.3 Insere os dados
insert_data.insert_navios(conn, navios)
insert_data.insert_tripulantes(conn, tripulantes)
insert_data.insert_empregados(conn, empregados)
insert_data.insert_movimentacoes(conn, movimentacoes)
insert_data.insert_movimentacoes_empregados(conn, movimentacoes_empregados)

# 2.4 Consultas
queries.query_n_of_tripulantes_emb(conn)
queries.query_emp_mov_id1(conn)
queries.query_quant_mov_cargueiro(conn)


# 2.6 Stored Procedure
stored_procedure.stored_procedure_empregado(conn)

# 2.5 Transação
transaction.transactions(conn)

# 2.7 Triggers
triggers.captain_trigger(conn)
triggers.manutencao_trigger(conn)
triggers.insert_mov_emp(conn)
triggers.check_tripulantes(conn)
triggers.insert_new_captains(conn)
triggers.insert_cap_trip3(conn)

conn.commit()
conn.close()