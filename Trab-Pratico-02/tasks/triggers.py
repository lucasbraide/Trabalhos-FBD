import psycopg2
from psycopg2 import sql
import db_config

def captain_trigger(conn):
    cursor = conn.cursor()

    check_capitao_func = """CREATE OR REPLACE FUNCTION validar_capitao()
                            RETURNS TRIGGER AS $$ 
                            BEGIN 
                            IF NEW.funcao = 'Capitão' AND EXISTS (SELECT 1 FROM Tripulantes T WHERE T.funcao = 'Capitão' AND NEW.id_emb = T.id_emb AND NEW.id_trp != T.id_trp) THEN
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
    
    if cursor is not None:
        cursor.close()

def manutencao_trigger(conn):
    cursor = conn.cursor()
    check_manutencao_func = """ CREATE OR REPLACE FUNCTION validar_manutencao()
                            RETURNS TRIGGER AS $body$
                            BEGIN 
                            IF (SELECT COUNT(*) FROM Movimentacoes WHERE id_mov = NEW.id_mov AND tipo = 'Manutenção') > 0 AND
                            (SELECT COUNT(*) FROM Empregados WHERE id_emp = NEW.id_emp AND funcao = 'Manutenção') = 0 
                            THEN RAISE EXCEPTION
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

# Tenta inserir os novas manutenções.
def insert_mov_emp(conn):
    cursor = conn.cursor()
    try:
        insert_mov_emp_5_5 = """INSERT INTO Movimentacoes_Empregados (id_mov,id_emp) VALUES 
                                (5,5);
                                """
        cursor.execute(insert_mov_emp_5_5)
        conn.commit()
        print("Movimentação 5 e empregado 5 interligados com sucesso, ambos possuem funções compativeis.")
    except psycopg2.DatabaseError as error:
        print("Movimentação 5 e empregado 5 não puderam ser interligados. Funções incompativeis.")


    try:
        insert_mov_emp_invalido = """INSERT INTO Movimentacoes_Empregados (id_mov,id_emp) VALUES 
                            (5,2);
                            """
        cursor.execute(insert_mov_emp_invalido)
        conn.commit()
        print("Movimentação 5 e empregado 2 interligados com sucesso, ambos possuem funções compativeis.")
    except psycopg2.DatabaseError as error:
        print("Movimentação 5 e empregado 2 não puderam ser interligados. Empregado não é de manutenção.")
    
    cursor.close()

def check_tripulantes(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tripulantes;")
    tripulantes = cursor.fetchall()
    print(tripulantes)
    cursor.close()

def insert_new_captains(conn):
    cursor = conn.cursor()
    try:
        insert_new_cap_emb4 = """INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES 
                            (7, 'Tripulante7', '1980-09-04', 'Capitão', 4); """
        cursor.execute(insert_new_cap_emb4)
        print("Capitão (tripulante de ID 7) adicionado a Embarcação de ID 4 com sucesso!")
        conn.commit()
    except psycopg2.DatabaseError as error:
        print("Não foi possível adicionar capitão a embarcação (possivelmente a embarcação já possui capitão.)")

    try:
        insert_new_cap_emb2 = """INSERT INTO Tripulantes(id_trp, nome, data_nasc, funcao, id_emb) VALUES 
                                (8, 'Tripulante8', '1985-03-03', 'Capitão', 2); """
        cursor.execute(insert_new_cap_emb2)
        print("Capitão (tripulante de ID 8) adicionado a Embarcação de ID 2 com sucesso!")
        conn.commit()
    except psycopg2.DatabaseError as error:
        print("Não foi possível adicionar capitão a embarcação (possivelmente a embarcação já possui capitão.)")
    cursor.close()

def insert_cap_trip3(conn):
    cursor=conn.cursor()
    try:
        insert_captain = """UPDATE Tripulantes SET funcao ='Capitão' WHERE nome='Tripulante3';"""
        cursor.execute(insert_captain)
        conn.commit()
    except psycopg2.DatabaseError as error:
        print("Não é possível atualizar função de para capitão - possivelmente a embarcação já possui capitão.")
    cursor.close()

