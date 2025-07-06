from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running!"


def run():
    app.run(host="0.0.0.0", port=2207)  # You can change the port if needed


def keep_alive():
    t = Thread(target=run)
    t.start()
