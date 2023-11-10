 print("Comando executado com sucesso: %s", query)

conn.commit()
cursor.close()
conn.close()