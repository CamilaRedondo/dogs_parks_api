from flask import Blueprint
from controllers.aux_controller import list_purposes, list_structures, list_accesses

aux_bp = Blueprint('aux', __name__)

@aux_bp.route('/finalidades/', methods=['GET'])
def purposes():
    return list_purposes()

@aux_bp.route('/estruturas/', methods=['GET'])
def structures():
    return list_structures()

@aux_bp.route('/tipos-acesso/', methods=['GET'])
def accesses():
    return list_accesses()
