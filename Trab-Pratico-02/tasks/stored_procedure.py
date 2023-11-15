import psycopg2
from psycopg2 import sql
import db_config

conn = db_config.db_conn()
cursor = conn.cursor()

try:
    # Criação do Stored Procedure empregado do mes que recebe como
    # parâmetro uma data e retorna o id e nome do empregado que participou de mais movimentações naquela
    # combinação Ano/Mês;
    cursor.execute("""CREATE OR REPLACE PROCEDURE empregado_do_mes (date DATE)
                    LANGUAGE SQL AS $$
                        SELECT E.id_emp, E.nome 
                        FROM Empregados e 
                        JOIN Movimentacoes_Empregados me ON e.id_emp = me.id_emp
                        JOIN Movimentacoes a ON a.id_mov = me.id_mov
                        WHERE a.data>= data_mov AND a.data < data_mov + INTERVAL '1 month' 
                        GROUP BY e.id_emp, e.nome 
                        ORDER BY COUNT(*) DESC 
                        LIMIT 1
                    $$""")

    # Chama o Stored Procedure
    cursor.execute("SELECT id_emp, nome FROM empregado_do_mes('2023-10-01')")
    empregado_do_mes = cursor.fetchall()

    # Printa o Stored Procedure
    print(empregado_do_mes)
    cursor.close()

except psycopg2.DatabaseError as error:
    print(error)
finally:
    if conn is not None:
        conn.close()