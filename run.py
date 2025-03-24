from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

from app.routes.book_routes import book_routes
from app.routes.main import main

app.register_blueprint(book_routes, url_prefix='/api')
app.register_blueprint(main)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
