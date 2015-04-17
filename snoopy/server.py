from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/info")
def info():
    return jsonify(status="Alive!")

def start_server():
    app.run(host="0.0.0.0")

if __name__ == "__main__":
	start_server()
