import socket
from flask import Flask, request

app = Flask(__name__)

@app.route("/hostname/")
def return_hostname():
    return "<p>Este ejemplo muestra la escalabilidad de una aplicación usando Docker.</p><br>La p&aacute;gina fue cargada desde el contenedor {}".format(socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0')