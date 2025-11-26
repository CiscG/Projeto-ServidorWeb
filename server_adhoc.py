from flask import Flask, render_template

app = Flask(__name__, template_folder="páginasHTML")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/camelo")
def camelo():
    return render_template("camelo.html")

# Rota para páginas HTML independentes
@app.route("/pagina/<nome>")
def pagina(nome):
    return render_template(f"{nome}.html")

# Todas as outras rotas enviam para o React
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, ssl_context="adhoc")