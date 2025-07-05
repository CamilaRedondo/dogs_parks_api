import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

DB_PATH = os.path.join(BASE_DIR, 'database', 'dogparks.db')
print("Caminho do banco:", DB_PATH)

def conectar():
    return sqlite3.connect(DB_PATH)

def getAllParks():
    conn = conectar()
    cursor = conn.cursor()

    query = """
    SELECT 
        p.id,
        p.name,
        a.street,
        a.city,
        a.state,
        a.postal_code,
        a.country,
        c.lat,
        c.long
    FROM park p
    LEFT JOIN address a ON p.address = a.id
    LEFT JOIN coordinate c ON a.coordinates = c.id
    """

    cursor.execute(query)
    colunas = [desc[0] for desc in cursor.description]
    resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]
    
    conn.close()
    return resultados

def deletePark(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM park WHERE id = ?", (id,))
    conn.commit()
    conn.close()