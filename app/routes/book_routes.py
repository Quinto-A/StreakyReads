from flask import Blueprint, request, jsonify
from app.models.book import Book
from app import db

main = Blueprint('main', __name__, url_prefix='/api')

@main.route('/')
def home():
    return jsonify({'message': 'Welcome to SteakyReads API!'})

@main.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(title=data['title'], author=data['author'], total_pages=data['total-pages'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

@main.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author, 'total_pages': book.total_pages, 'pages_read': book.pages_read} for book in books])

@main.route('/books/<int:book_id>/progress', methods=['PATCH'])
def update_progress(book_id):
    data = request.json
    book = Book.query.get_or_404(book_id)
    book.pages_read = min(book.pages_read + data['pages_read'], book.total_pages)
    db.session.commit()
    return jsonify({'message': 'Progress updated successfully'})
