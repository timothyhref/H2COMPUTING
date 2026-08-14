from flask import *
app = Flask(__name__)
@app.route("/")
def index():
    colour = {"000":"red","001":"white","010":"yellow","011":"blue","100":"black","110":"green"}
    with open("decompressedimage.txt","r") as file:
        lines = file.readlines()
        #with automatically closes
    lines = [colour[line.strip()] for line in lines]
    return render_template("index.html",lines = lines)
if (__name__) == "__main__":
    app.run(debug=True, port=5000)