from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    total_pages = db.Column(db.Integer, nullable=False)
    pages_read = db.Column(db.Integer, default=0)
