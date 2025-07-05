from .database import conectar

def get_countries():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT country FROM address WHERE country IS NOT NULL")
    paises = [row[0] for row in cursor.fetchall()]
    conn.close()
    return paises

def get_states_by_country(pais):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT state FROM address WHERE country = ? AND state IS NOT NULL", (pais,))
    estados = [row[0] for row in cursor.fetchall()]
    conn.close()
    return estados

def get_cities_by_state_and_country(estado, pais):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT city FROM address
        WHERE state = ? AND country = ? AND city IS NOT NULL
    """, (estado, pais))
    cidades = [row[0] for row in cursor.fetchall()]
    conn.close()
    return cidades

def get_all_address():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.id, a.street, a.city, a.state, a.postal_code, a.country, c.lat, c.long
        FROM address a
        JOIN coordinate c ON a.coordinates = c.id
    """)
    resultado = [
        {
            "id": row[0],
            "street": row[1],
            "city": row[2],
            "state": row[3],
            "postal_code": row[4],
            "country": row[5],
            "lat": row[6],
            "long": row[7]
        }
        for row in cursor.fetchall()
    ]
    conn.close()
    return resultado
