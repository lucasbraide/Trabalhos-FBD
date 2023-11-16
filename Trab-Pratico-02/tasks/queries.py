import psycopg2
from psycopg2 import sql

def query_n_of_tripulantes_emb(conn): 
    cursor = conn.cursor()

    # 1- Retorne todas as embarcações e o número de tripulantes de cada embarcação.
    cursor.execute("SELECT E.nome AS nome_embarcacao, COUNT(T.id_trp) as numero_tripulantes FROM Embarcacoes E JOIN Tripulantes T ON E.id_emb = T.id_emb GROUP BY E.nome")

    tripulantes_embarcacao = cursor.fetchall()

    print("1- Retorne todas as embarcações e o número de tripulantes de cada embarcação.")
    for item in tripulantes_embarcacao:
        print(item)

    cursor.close()

def query_emp_mov_id1(conn):
    cursor = conn.cursor()

    #2- Retorne os Empregados envolvidos na movimentação de ID 1.

    cursor.execute("SELECT e.nome FROM Empregados e JOIN Movimentacoes_Empregados me ON e.id_emp = me.id_emp WHERE me.id_mov = 1;")
    emp_mov_id1 = cursor.fetchall()
    for item in emp_mov_id1:
        print(item)

def query_quant_mov_cargueiro(conn):
    cursor = conn.cursor()
    #3- Retorne a quantidade de movimentações que envolvem embarcações do tipo 'Cargueiro'.

    cursor.execute("SELECT COUNT(*) AS quant FROM Movimentacoes m JOIN Embarcacoes e ON m.id_emb = e.id_emb WHERE e.tipo = 'Cargueiro'")
    quant_mov_cargueiro =  cursor.fetchall()

    for item in quant_mov_cargueiro:
        print(item)
    