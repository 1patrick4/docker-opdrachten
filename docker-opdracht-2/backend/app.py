from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify(status="yes")

@app.route("/api")
def wegaan():
    return jsonify(status="joe")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)