from flask import jsonify
from models.aux_model import get_purposes, get_structures, get_accesses

def list_purposes():
    return jsonify(get_purposes())

def list_structures():
    return jsonify(get_structures())

def list_accesses():
    return jsonify(get_accesses())

