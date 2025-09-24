from flask import Blueprint
from controllers.aux_controller import list_purposes, list_structures, list_accesses

aux_bp = Blueprint('aux', __name__)

@aux_bp.route('/finalidades/', methods=['GET'])
def purposes():
    """
    Lista de finalidades possíveis para parques
    ---
    responses:
      200:
        description: Lista de finalidades
        examples:
          application/json: [
            {"id": 1, "name": "Adestramento"},
            {"id": 2, "name": "Recreação"},
            {"id": 3, "name": "Esporte"}
          ]
    """
    return list_purposes()

@aux_bp.route('/estruturas/', methods=['GET'])
def structures():
    """
    Lista de estruturas possíveis para parques
    ---
    responses:
      200:
        description: Lista de estruturas
        examples:
          application/json: [
            {"id": 1, "name": "Externo"},
            {"id": 2, "name": "Coberto"},
            {"id": 3, "name": "Área cercada"}
          ]
    """
    return list_structures()

@aux_bp.route('/tipos-acesso/', methods=['GET'])
def accesses():
    """
    Lista de tipos de acesso possíveis para parques
    ---
    responses:
      200:
        description: Lista de tipos de acesso
        examples:
          application/json: [
            {"id": 1, "name": "Público"},
            {"id": 2, "name": "Privado"},
            {"id": 3, "name": "Misto"}
          ]
    """
    return list_accesses()