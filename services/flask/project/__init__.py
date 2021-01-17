from flask import Flask, jsonify, render_template


app = Flask(__name__)


#@app.route("/about")
@app.route("/")
def hello_world():
    #return jsonify(hello="world")
    return render_template("embed.html")