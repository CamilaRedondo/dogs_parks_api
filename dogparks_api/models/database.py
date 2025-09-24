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
        c.long,
        ac.name AS access_name,
        ac.description AS access_description,
        GROUP_CONCAT(DISTINCT pu.name) AS purposes,
        GROUP_CONCAT(DISTINCT st.name) AS structures
    FROM park p
    LEFT JOIN address a ON p.address = a.id
    LEFT JOIN coordinate c ON a.coordinates = c.id
    LEFT JOIN access ac ON p.access = ac.id
    LEFT JOIN park_purposes pp ON p.id = pp.id_park
    LEFT JOIN purpose pu ON pp.id_purpose = pu.id
    LEFT JOIN park_structure ps ON p.id = ps.id_park
    LEFT JOIN structure st ON ps.id_structure = st.id
    GROUP BY 
        p.id, p.name, a.street, a.city, a.state, a.postal_code, 
        a.country, c.lat, c.long, ac.name, ac.description
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