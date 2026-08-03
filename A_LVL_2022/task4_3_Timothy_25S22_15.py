from flask import *
import sqlite3
query = '''SELECT member.FamilyName,member.GivenName,book.Title
FROM (Member JOIN Loan ON Member.MemberNumber=Loan.MemberNumber) AS link
JOIN book ON link.BookID = book.BookID
WHERE loan.returned = 'FALSE' '''
app = Flask(__name__)
@app.route("/")
def index():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.close()
    return render_template("index.html",unreturned=result)
if __name__ == "__main__":
    app.run()