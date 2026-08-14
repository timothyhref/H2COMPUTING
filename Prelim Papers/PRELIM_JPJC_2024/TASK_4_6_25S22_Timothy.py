from flask import *
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("menu.html")

@app.route("/arrival")
def arrival():
    conn = sqlite3.connect("Airport.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT arrivalTime, departure, flightNum FROM Flight WHERE destination = "Singapore (SIN)"''')
    result = cursor.fetchall()
    conn.close()
    return render_template('arrival.html',data = result)

@app.route("/departure")
def departure():
    conn = sqlite3.connect("Airport.db")
    cursor = conn.cursor()
    cursor.execute('''SELECT departureTime, destination, flightNum FROM Flight WHERE departure = "Singapore (SIN)"''')
    result = cursor.fetchall()
    conn.close()
    return render_template('departure.html',data = result)

@app.route("/query", methods = ["GET","POST"])
def query():
    if request.method == "GET":
        return render_template("form.html")
    conn = sqlite3.connect("Airport.db")
    cursor = conn.cursor()
    query = request.form.get("flightNum")
    cursor.execute('''SELECT * FROM Flight WHERE flightNum = ?''',(query,))
    result = cursor.fetchall()
    conn.close()
    return render_template("query_result.html",data = result)

if __name__ == "__main__":
    app.run(debug = True)

