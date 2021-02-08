from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "main":
    app.debug(True)

@app.route('/')
def home():
    return render_template('index.html', test_var="Coming from the server you get it?")



