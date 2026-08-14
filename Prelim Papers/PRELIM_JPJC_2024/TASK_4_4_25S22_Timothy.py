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
if __name__ == "__main__":
    app.run(debug = True)