from flask import Flask
from flask.cli import routes_command
import check_port

app = Flask(__name__)

@ app.route("/hello")
def hello():
    return "Hello"


@app.route("/hi")
def hi(): 
    return "Hi"


@app.route('/port/<ip>/<port>/')
def test(ip: str, port: int):
    if check_port.is_open(ip, port):
        return "Porta Aberta"
    else:
        return "Porta Fechada"

 


app.run(debug="True")