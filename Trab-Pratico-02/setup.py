import psycopg2
from psycopg2 import sql
import db_config

def setup_tables(conn):
    ''' Realiza a limpeza do banco de dados. '''
    cursor = conn.cursor()
    
    # Exclui e reseta todas as tabelas
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        truncate_query = sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY CASCADE").format(sql.Identifier(table_name))
        drop_query = sql.SQL("DROP TABLE IF EXISTS {} CASCADE").format(sql.Identifier(table_name))
        cursor.execute(truncate_query)
        cursor.execute(drop_query)

    print("Setup executado com sucesso.")
    conn.commit()
    cursor.close()