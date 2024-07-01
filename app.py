from flask import Flask, render_template
import os
import random

app = Flask(__name__)


images = [
    "https://raw.githubusercontent.com/lidorg-dev/cats-images/main/images/image1.gif",
    "https://raw.githubusercontent.com/lidorg-dev/cats-images/main/images/image2.gif",
    "https://raw.githubusercontent.com/lidorg-dev/cats-images/main/images/image3.gif",
    "https://raw.githubusercontent.com/lidorg-dev/cats-images/main/images/image4.gif",
    "https://raw.githubusercontent.com/lidorg-dev/cats-images/main/images/image5.gif"
]

@app.route("/")
def index():
    src = random.choice(images)
    return render_template("index.html", url=src)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
