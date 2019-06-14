from . import db

class Note(db.Model):
    __tablename__ = 'notes' 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.title