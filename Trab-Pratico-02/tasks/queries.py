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