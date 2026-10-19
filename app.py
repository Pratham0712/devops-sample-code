from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Jenkins Multi-Stage Pipeline!"


if __name__ == "__main__":
    # No debug=True: the reloader forks a child, so the PID we save would be wrong
    app.run(host="127.0.0.1", port=5000)
