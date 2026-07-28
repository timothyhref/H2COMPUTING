from flask import *
import sqlite3

app = Flask(__name__)
@app.route("/")
def index():
    people = []
    with open("people.txt","r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(",")
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT FullName, ScreenName FROM People")
    result = cursor.fetchall()
    conn.close()
    for i in range(len(result)):
        people.append(tuple([result[i][0],result[i][1],lines[i][2]]))

    return render_template("page.html",people=people)

if __name__ == "__main__":
    app.run()