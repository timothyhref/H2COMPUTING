from flask import *
import sqlite3
app = Flask(__name__)
@app.route('/',methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    else:
        name = request.form.get("customer_name")
        conn = sqlite3.connect("COURSES.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Course.Name, Instructor.Name, Registration.Paid FROM Registration JOIN Course On Registration.CourseID = Course.CourseID JOIN Instructor ON Instructor.InstructorID = Course.InstructorID JOIN Customer ON Registration.CustomerID = Customer.CustomerID WHERE Customer.Name = ?''',(name,))
        results = cursor.fetchall()
        if results == []:
            results = False
        return render_template("display.html",results=results)
if '__main__' == (__name__):
    app.run(debug=True)

