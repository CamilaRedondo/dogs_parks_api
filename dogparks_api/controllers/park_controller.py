from flask import jsonify
from models.database import getAllParks, deletePark
from models.park_model import updatePark, create_new_park

def park_list():
    parques = getAllParks()
    return jsonify(parques)

def delete_park(id):
    deletePark(id)
    return jsonify({"mensagem": f"Parque {id} excluído com sucesso."})

def update_park(id, data):
    updatePark(id, data)
    return jsonify({"mensagem": f"Parque {id} atualizado com sucesso."})

def create_park(data):
    id_gerado = create_new_park(data)
    return jsonify({"mensagem": "Parque criado com sucesso.", "id": id_gerado})