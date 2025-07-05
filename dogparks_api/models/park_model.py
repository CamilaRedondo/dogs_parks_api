from .database import conectar

def updatePark(id_park, data):
    conn = conectar()
    cursor = conn.cursor()

    # Atualizar tabela park
    cursor.execute("UPDATE park SET name = ?, access = ? WHERE id = ?", 
                   (data['name'], data['access'], id_park))

    # Buscar ID do endereço atual do parque
    cursor.execute("SELECT address FROM park WHERE id = ?", (id_park,))
    id_address = cursor.fetchone()[0]

    # Buscar ID das coordenadas
    cursor.execute("SELECT coordinates FROM address WHERE id = ?", (id_address,))
    id_coords = cursor.fetchone()[0]

    # Atualizar endereço
    addr = data['address']
    cursor.execute("""
        UPDATE address SET 
            street = ?, city = ?, state = ?, postal_code = ?, country = ?
        WHERE id = ?
    """, (addr['street'], addr['city'], addr['state'], addr['postal_code'], addr['country'], id_address))

    # Atualizar coordenadas
    cursor.execute("""
        UPDATE coordinate SET 
            lat = ?, long = ?
        WHERE id = ?
    """, (addr['lat'], addr['long'], id_coords))

    # Atualizar estruturas
    cursor.execute("DELETE FROM park_structure WHERE id_park = ?", (id_park,))
    for structure_id in data.get('structures', []):
        cursor.execute("INSERT INTO park_structure (id_park, id_structure) VALUES (?, ?)", 
                       (id_park, structure_id))

    # Atualizar finalidades
    cursor.execute("DELETE FROM park_purposes WHERE id_park = ?", (id_park,))
    for purpose_id in data.get('purposes', []):
        cursor.execute("INSERT INTO park_purposes (id_park, id_purpose) VALUES (?, ?)", 
                       (id_park, purpose_id))

    conn.commit()
    conn.close()


def create_new_park(data):
    conn = conectar()
    cursor = conn.cursor()

    addr = data['address']

    # 1. Criar coordenadas
    cursor.execute("INSERT INTO coordinate (lat, long) VALUES (?, ?)", (addr['lat'], addr['long']))
    id_coords = cursor.lastrowid

    # 2. Criar endereço
    cursor.execute("""
        INSERT INTO address (street, city, state, postal_code, country, coordinates)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (addr['street'], addr['city'], addr['state'], addr['postal_code'], addr['country'], id_coords))
    id_address = cursor.lastrowid

    # 3. Criar parque
    cursor.execute("""
        INSERT INTO park (name, address, access)
        VALUES (?, ?, ?)
    """, (data['name'], id_address, data['access']))
    id_park = cursor.lastrowid

    # 4. Associar estruturas
    for structure_id in data.get('structures', []):
        cursor.execute("INSERT INTO park_structure (id_park, id_structure) VALUES (?, ?)", 
                       (id_park, structure_id))

    # 5. Associar finalidades
    for purpose_id in data.get('purposes', []):
        cursor.execute("INSERT INTO park_purposes (id_park, id_purpose) VALUES (?, ?)", 
                       (id_park, purpose_id))

    conn.commit()
    conn.close()

    return id_park
