from .database import conectar

def get_purposes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, code, name, description FROM purpose")
    dados = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return dados

def get_structures():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, code, name, description FROM structure")
    dados = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return dados

def get_accesses():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, code, name, description FROM access")
    dados = [dict(zip([col[0] for col in cursor.description], row)) for row in cursor.fetchall()]
    conn.close()
    return dados

