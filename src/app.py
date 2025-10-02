from flask import Flask , jsonify , render_template
import socket

def fetchhostdetails():
     hostname = str(socket.gethostname())
     ip = str(socket.gethostbyname(hostname))
     return hostname,ip

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
     return jsonify(
          status = "UP"
     )
@app.route("/details")
def details():
    hostname , ip = fetchhostdetails()
    return render_template('index.html', HOSTNAME = hostname , IP = ip)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)