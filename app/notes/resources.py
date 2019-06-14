from . import notes
from flask import jsonify

@notes.route('/')
def index():
    return jsonify({'123':'123'})