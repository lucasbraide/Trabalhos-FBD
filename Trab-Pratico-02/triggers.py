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

check_capitao_func = """CREATE OR REPLACE FUNCTION validar_capitao()
                        RETURNS TRIGGER AS $$ 
                        BEGIN 
                        IF NEW.funcao = 'Capitão' AND EXISTS (SELECT 1 FROM Tripulantes T WHERE T.funcao = 'Capitão' AND NEW.id_emb = T.id_emb) THEN
                        RAISE EXCEPTION 'Não é possível cadastrar um novo capitão - já tem um capitão cadastrado.';
                        END IF;
                        RETURN NEW;
                        END; $$ LANGUAGE plpgsql;"""

capitao_trigger = """CREATE TRIGGER trg_tripulante_check_capitao
                        BEFORE INSERT OR UPDATE OF funcao ON Tripulantes
                        FOR EACH ROW EXECUTE FUNCTION validar_capitao();"""

try:
    # 1. Cria a função de checar validade da adição de novo capitão
    cursor.execute(check_capitao_func)

    # 2. Cria o trigger de INSERT ou UPDATE capitão em tripulantes 
    cursor.execute(capitao_trigger)

    conn.commit()
    print("Função e Trigger de verificação de capitão implementadas com sucesso.")

except psycopg2.DatabaseError as error:
    print(error)


check_manutencao_func = """ CREATE OR REPLACE FUNCTION validar_manutencao()
                            RETURNS TRIGGER AS $body$
                            BEGIN 
                            IF NEW.id_mov IN (SELECT * FROM Movimentacoes WHERE tipo = 'Manutenção') AND
                            NEW.id_emp NOT IN (SELECT * FROM Empregados WHERE funcao = 'Manutenção') THEN RAISE EXCEPTION
                            'Não é possível alocar Empregado na Movimentação - Movimentações de manutenção só podem ser executadas
                            por funcionários de manutenção';
                            END IF;
                            RETURN NEW;  
                            END; $body$ LANGUAGE plpgsql"""

check_manutencao_trigger = """CREATE TRIGGER trg_movimentacao_manutencao_check BEFORE 
                              INSERT OR UPDATE ON Movimentacoes_Empregados 
                              FOR EACH ROW EXECUTE FUNCTION validar_manutencao()"""

try:
    # 1. Cria a função de checar validade da adição de nova movimentação com manutenção
    cursor.execute(check_manutencao_func)

    # 2. Cria o trigger de INSERT ou UPDATE na tabela Movimentacao_Empregados
    cursor.execute(check_manutencao_trigger)

    conn.commit()
    print("Função e Trigger de verificação de equipe de manutenção implementadas com sucesso.")
except psycopg2.DatabaseError as error:
    print(error)

if cursor is not None:
    cursor.close()

if conn is not None:
    conn.close()