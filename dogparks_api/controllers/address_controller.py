from flask import jsonify, request
from models.address_model import (
    get_countries,
    get_states_by_country,
    get_cities_by_state_and_country,
    get_all_address
)

def list_countries():
    return jsonify(get_countries())

def list_states():
    pais = request.args.get('pais')
    if not pais:
        return jsonify({"erro": "Parâmetro 'pais' obrigatório"}), 400
    return jsonify(get_states_by_country(pais))

def list_cities():
    estado = request.args.get('estado')
    pais = request.args.get('pais')
    if not estado or not pais:
        return jsonify({"erro": "Parâmetros 'estado' e 'pais' obrigatórios"}), 400
    return jsonify(get_cities_by_state_and_country(estado, pais))

def list_address():
    return jsonify(get_all_address())
