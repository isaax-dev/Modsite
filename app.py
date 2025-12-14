from flask import Flask

# cria a aplicação
app = Flask(__name__)

# rota principal
@app.route("/")
def home():
    return "Modsite online 🔥"

# roda o servidor
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
