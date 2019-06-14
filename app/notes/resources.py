from . import notes
from ..models import Note
from flask import jsonify

@notes.route('/')
def get_list():
    notes = Note.query.all()
    result = [dict(note) for note in notes]
    return jsonify(result)

@notes.route('/', methods=['POST'])
def create():
    return jsonify({})