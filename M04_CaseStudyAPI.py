#Name: Doris Tran
#Date: September 18, 2022
#M04 Lab - Case Study Python API
#Make a CRUD API for Book based on the tutorial

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#My database to store book information
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Lab_Book.db'
db = SQLAlchemy(app)

#Make a class for Book
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100))

    def __repr__(self):
        return f"\nBook {self.id}  \nTitle: {self.book_name} \nAuthor: {self.author} \nPublisher: {self.publisher}\n"

@app.route('/')
def index():
    return 'Hello. This is my webpage for my books'

#List books
@app.route('/book')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'title': book.book_name, 'author': book.author, 'publisher':book.publisher}
        output.append(book_data)

    return {'book':output}

#Get a book and its information by id
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return{"title" : book.book_name, "author" : book.author, "publisher" : book.publisher}

#Enter a new book with its information
@app.route('/books', methods = ['POST'])
def add_book():
    book = Book(book_name = request.json['title'], author = request.json['author'], publisher = request.json['publisher']) #make a new book
    db.session.add(book)
    db.session.commit()
    return {'id': book.id} 

#Remove book by its id
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "404 - Not Found!"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "The book has been removed."}