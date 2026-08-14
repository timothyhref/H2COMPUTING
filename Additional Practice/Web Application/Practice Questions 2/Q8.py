from flask import *
app = Flask(__name__)
@app.route("/greet")
def greet():
    name = request.args.get("name")
    return render_template("Q8.html",name = name)
if __name__ == "__main__":
    app.run(debug=True)