from flask import Flask, render_template, request, jsonify
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = MobileNetV2(weights="imagenet")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/judge", methods=["POST"])
def judge():
    if "image" not in request.files:
        return jsonify({"judgment": "No image uploaded!"})

    img_file = request.files["image"]
    img = Image.open(img_file.stream).convert("RGB")
    img = img.resize((224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    decoded = decode_predictions(preds, top=3)[0]
    labels = [label.lower() for (_, label, _) in decoded]

    judgment = get_judgment(labels)
    return jsonify({"judgment": judgment})

def get_judgment(labels):
    if any(word in labels for word in ['suit', 'blazer']):
        return "Serving business realness! 💼"
    elif any(word in labels for word in ['t-shirt', 'jeans']):
        return "Chill and comfy. Nice!"
    elif any(word in labels for word in ['clown']):
        return "You’re bold... 😳"
    elif any(word in labels for word in ['kimono', 'robe']):
        return "Cultural + classy ✨"
    else:
        return "Unique... in your own way 😉"

if __name__ == "__main__":
    app.run(debug=True)
