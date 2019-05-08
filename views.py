"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from flask import jsonify 


books = [
    {
        'name' : 'firstBook',
        'price' : 1,
        'isbn' : 1111
    },
    {
        'name' : 'SecondName',
        'price' : 2,
        'isbn' : 2222
    }
]


@app.route('/') 
@app.route('/hoba') 
@app.route('/cha') 
def index():
    return jsonify({'Who is jopa?' : 'you are'})


@app.route('/books')
def get_all_books():
    return jsonify({'books' : books})

@app.route('/<int:isbn>') 
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    for i in books:
        if i['isbn'] == isbn:
            return jsonify({'name' : i['name'], 'price' : i['price']})
