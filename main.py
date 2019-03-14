import socket
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hostname/")
def return_hostname():
    return render_template('index.html', container = socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')