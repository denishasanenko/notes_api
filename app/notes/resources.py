from . import notes
from .. import db
from ..models import Note, notes_schema, note_schema
from flask import jsonify, request
from marshmallow import ValidationError

@notes.route('/')
def get_list():
    notes_query = list(Note.query.all())
    notes_list = notes_schema.dump(notes_query)
    return jsonify(notes_list.data)

@notes.route('/', methods=['POST'])
def create():
    json_data = request.json
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    try:
        data = note_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    note = Note(title=data.data['title'])
    db.session.add(note)
    db.session.commit()
    return jsonify(note_schema.dump(note).data)