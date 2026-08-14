from flask import *
import sqlite3


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/1")
def round_1():
    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    names = cursor.execute("SELECT competitor.name,scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 1 ORDER BY scores.score DESC").fetchall()
    return render_template("results.html",names=names)
@app.route("/2")
def round_2():
    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    names = cursor.execute("SELECT competitor.name,scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 2 ORDER BY scores.score DESC").fetchall()
    return render_template("results.html",names=names)
@app.route("/3")
def round_3():
    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    names = cursor.execute("SELECT competitor.name,scores.score FROM competitor INNER JOIN scores ON competitor.id = scores.id WHERE scores.round = 3 ORDER BY scores.score DESC").fetchall()
    return render_template("results.html",names=names)
@app.route("/mean")
def mean():
    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    result = cursor.execute('''SELECT competitor.name, ROUND(AVG(scores.score),2) AS mean
FROM competitor join scores on competitor.id = scores.id
GROUP BY competitor.id
ORDER BY competitor.name ASC''').fetchall()
    return render_template("mean.html", people = result)
@app.route("/quals")
def quals():
    conn = sqlite3.connect("Task4.db")
    cursor = conn.cursor()
    result = cursor.execute('''SELECT competitor.name, SUM(scores.score) AS totality, (SUM(scores.score) > 250) AS qual
FROM competitor join scores on competitor.id = scores.id
GROUP BY competitor.id ORDER BY totality DESC''').fetchall()
    return render_template("quals.html",people = result)
if __name__ == "__main__":
    app.run(debug=True)