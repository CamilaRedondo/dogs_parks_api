from flask import Blueprint, request
from controllers.park_controller import park_list, delete_park, update_park, create_park

park_bp = Blueprint('parque', __name__, url_prefix='/parques')

@park_bp.route('/', methods=['GET'])
def get_parks():
    """
    Lista todos os parques
    ---
    responses:
      200:
        description: Lista de parques
        examples:
          application/json: [{ "access_description": "Acesso livre ao público", "access_name": "Público", "city": "São José dos Campos", "country": "Brasil", "id": 5, "lat": -23.2028815, "long": -45.8926323, "name": "Parque Coberto Dog", "postal_code": "80000-000", "purposes": "Adestramento", "state": "SP", "street": "Nassau", "structures": "Externo" }]
    """
    return park_list()

@park_bp.route('/<int:id>', methods=['DELETE'])
def deletePark(id):
    """
    Deleta um parque
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do parque
    responses:
      200:
        description: Parque removido com sucesso
      404:
        description: Parque não encontrado
    """
    return delete_park(id)

@park_bp.route('/<int:id>', methods=['PUT'])
def updatePark(id):
    """
    Atualiza um parque existente
    ---
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: ID do parque
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            access:
              type: string
            address:
              type: object
              properties:
                street: { type: string }
                city: { type: string }
                state: { type: string }
                postal_code: { type: string }
                country: { type: string }
                lat: { type: number, format: float }
                long: { type: number, format: float }
            structures:
              type: array
              items: { type: integer }
            purposes:
              type: array
              items: { type: integer }
    responses:
      200:
        description: Parque atualizado com sucesso
      404:
        description: Parque não encontrado
    """
    data = request.json
    return update_park(id, data)


@park_bp.route('/', methods=['POST'])
def newPark():
    """
    Cria um novo parque
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - access
            - address
          properties:
            name:
              type: string
              example: "Parque Central"
            access:
              type: string
              example: "Público"
            address:
              type: object
              properties:
                street:
                  type: string
                  example: "Rua das Flores"
                city:
                  type: string
                  example: "São Paulo"
                state:
                  type: string
                  example: "SP"
                postal_code:
                  type: string
                  example: "01000-000"
                country:
                  type: string
                  example: "Brasil"
                lat:
                  type: number
                  format: float
                  example: -23.55052
                long:
                  type: number
                  format: float
                  example: -46.633308
            structures:
              type: array
              items:
                type: integer
              example: [1, 2, 3]
            purposes:
              type: array
              items:
                type: integer
              example: [1]
    responses:
      201:
        description: Parque criado com sucesso
    """
    data = request.json
    return create_park(data)