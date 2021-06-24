from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "inital creation of page status: success"


