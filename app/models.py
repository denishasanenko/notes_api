from . import db
from marshmallow import Schema, fields

class Note(db.Model):
    __tablename__ = 'notes' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.title

class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)