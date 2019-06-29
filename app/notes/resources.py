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

@notes.route('/<id>')
def get_one(id):
    note_row = Note.query.filter_by(id=id).first()
    if not note_row:
        return "", 404
    note = note_schema.dump(note_row)
    return jsonify(note.data)

@notes.route('/', methods=['POST'])
def create():
    json_data = request.json
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    try:
        data = note_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    note = Note(title=data.data['title'], note=data.data['note'])
    db.session.add(note)
    db.session.commit()
    return jsonify(note_schema.dump(note).data)


@notes.route('/<id>', methods=['PUT'])
def update(id):
    json_data = request.json
    if not json_data:
        return jsonify({'message': 'No input data provided'}), 400

    try:
        data = note_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    note = Note.query.filter_by(id=id).first()
    print(note)
    if not note:
        return "", 404
    note.title = data.data['title']
    note.note = data.data['note']
    db.session.add(note)
    db.session.commit()
    return jsonify(note_schema.dump(note).data)