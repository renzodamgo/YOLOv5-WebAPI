"""
Simple app to upload an image via a web form
and view the inference results on the image in the browser.
"""
from flask import Flask, redirect, render_template, request

import argparse
# import io
import os
from inference import get_prediction

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()

        get_prediction(img_bytes)
        #img = Image.open(io.BytesIO(img_bytes))
        #results = model(img, size=640)

        # for debugging
        # data = results.pandas().xyxy[0].to_json(orient="records")
        # return data


        return redirect("static/image0.jpg")

    return render_template("index.html")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()
    print("modelo cargado")
    app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
