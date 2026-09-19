from flask import *
import sqlite3
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "GET":
        return render_template("form.html")
    else:
        code = request.form.get("code")
        conn = sqlite3.connect("BUSROUTES.db")
        cursor = conn.cursor()
        cursor.execute("SELECT ServiceNo,Operator FROM Route WHERE BusStopCode =  ?",(code,))
        result = cursor.fetchall()
        if len(result) == 0:
            result = False
        return render_template("display.html",result = result)
if "__main__" == (__name__):
    app.run(debug=True)