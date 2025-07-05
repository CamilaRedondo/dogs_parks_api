from flask import Blueprint, request
from controllers.park_controller import park_list, delete_park, update_park, create_park

park_bp = Blueprint('parque', __name__, url_prefix='/parques')

@park_bp.route('/', methods=['GET'])
def get_parks():
    return park_list()

@park_bp.route('/<int:id>', methods=['DELETE'])
def deletePark(id):
    return delete_park(id)

@park_bp.route('/<int:id>', methods=['PUT'])
def updatePark(id):
    data = request.json
    return update_park(id, data)


@park_bp.route('/', methods=['POST'])
def newPark():
    data = request.json
    return create_park(data)