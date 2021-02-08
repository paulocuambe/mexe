from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Home"


if __name__ == "main":
    app.debug(True)
