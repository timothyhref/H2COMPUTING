from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOOK")
    books = cursor.fetchall()
    conn.close()
    return render_template("index.html",books = books)

@app.route("/book/<int:book_id>")
def find_book(book_id):
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM BOOK WHERE bookID = ?''',(book_id,))
    result = cursor.fetchall()
    conn.close()
    if result == []:
        return "<h1>Book not found</h1>"
    else:
        return render_template("index.html",books = result)

@app.route("/expensive")
def expensive():
    conn = sqlite3.connect("bookstore.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM BOOK WHERE price > 20''')
    books = cursor.fetchall()
    conn.close()
    return render_template("index.html",books = books)


if __name__ == "__main__":
    app.run(debug=True)
