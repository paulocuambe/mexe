from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', test_var="Coming from the server")


if __name__ == "main":
    app.debug(True)
