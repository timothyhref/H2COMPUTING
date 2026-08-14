from flask import *
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("image_upload.html")
@app.route("/upload_image",methods = ['POST'])
def upload_image():
    file = request.files["myfile"] #.files returns a dictionary
    filename = file.filename
    file.save("Claude_GET&POST_File_Upload/static/images/"+filename)
    return "Image saved as "+filename
if __name__ == "__main__":
    app.run(debug = True)