from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

ovocie = ["jablko","pomaranc","jahoda"]

@app.route("/", methods=["GET"])
def main():
    return jsonify({"ovocie":ovocie}),200

if __name__ == "__main__":
    app.run()
