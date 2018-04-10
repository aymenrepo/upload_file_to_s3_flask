from flask import Flask, render_template, request, redirect
from werkzeug.security import secure_filename
from .resource import *
app = Flask(__name__)
app.config.from_object("flask_s3_upload.config")


@app.route("/", methods=["POST"])
def upload_file():
    """
    upload file : main function
    :return:
    """

    if "user_file" not in request.files:
        return "No user_file key in request.files"
    file = request.files["user_file"]

    """
        These attributes are also available

        file.filename               # The actual name of the file
        file.content_type
        file.content_length
        file.mimetype

    """
    if file.filename == "":
        return "Please select a file"

    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")