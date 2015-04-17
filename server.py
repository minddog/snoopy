from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/info")
def info():
    return jsonify(status="Alive!")

if __name__ == "__main__":
    app.run()
