from flask import *
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("Q9_form.html")
@app.route("/read", methods = ["GET"])
def read():
    colour = request.args.get("colour")
    return render_template("Q9_colour.html",colour = colour)
if __name__ == "__main__":
    app.run()