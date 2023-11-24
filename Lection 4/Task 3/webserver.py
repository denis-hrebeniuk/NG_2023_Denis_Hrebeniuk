import os
from flask import Flask, render_template, request

app = Flask(__name__)


def get_all_images():
    images = []

    for file_name in os.listdir("static/images/"):
        if ".jpg" in file_name or ".png" in file_name:
            images.append(file_name)

    return images


gallery = get_all_images()


@app.route("/")
def index():
    return render_template("index.html", image_index=0, image_name=gallery[0])


@app.route("/changeimage")
def change_image():
    image_index = int(request.args.get("image_index"))
    action = request.args.get("action")

    match action:
        case "previous":
            image_index -= 1
        case "next":
            image_index += 1

    if image_index < 0 or image_index >= len(gallery):
        image_index = 0

    return render_template(
        "index.html", image_index=image_index, image_name=gallery[image_index]
    )


app.run(host="0.0.0.0", port=8080)
