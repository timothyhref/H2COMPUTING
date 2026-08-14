from flask import *
app = Flask(__name__)
@app.route("/search/<string:s>")
def search(s):
    return "Searching for "+s
