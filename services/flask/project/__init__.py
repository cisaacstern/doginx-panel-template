from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/about")
def hello_world():
    return jsonify(hello="world")
