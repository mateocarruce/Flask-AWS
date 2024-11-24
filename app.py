from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola desde AWS EC2 y GitHub Actions!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
