# app.py

from flask import Flask, render_template, request, redirect  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://myapp:password@localhost/library_db'

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.name}>'

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)  

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        price = request.form['price']

        new_book = Book(name=name, author=author, price=price)
        db.session.add(new_book)
        db.session.commit()

        return redirect('/')

    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = Book.query.get(book_id)
    
    if request.method == 'POST':
        book.name = request.form['name']
        book.author = request.form['author']
        book.price = request.form['price']
        db.session.commit()
        return redirect('/')
        
    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)