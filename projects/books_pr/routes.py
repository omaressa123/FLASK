from flask import Blueprint, render_template
from app import db
from app.model import Book

main = Blueprint('main', __name__)

@main.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@main.route('/about')
def about():
    return render_template('about.html')
