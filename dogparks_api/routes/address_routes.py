from flask import Blueprint
from controllers.address_controller import (
    list_countries,
    list_states,
    list_cities,
    list_address
)

address_bp = Blueprint('enderecos', __name__)

address_bp.route('/paises/', methods=['GET'])(list_countries)
address_bp.route('/estados/', methods=['GET'])(list_states)
address_bp.route('/cidades/', methods=['GET'])(list_cities)
address_bp.route('/enderecos/', methods=['GET'])(list_address)
