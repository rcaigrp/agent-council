from flask import Flask, render_template, jsonify
from app.utils.scan import scan_network

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan")
def scan():
    devices = scan_network()
    return jsonify(devices)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)