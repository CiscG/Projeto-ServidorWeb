from flask import Flask, render_template

app = Flask(__name__, template_folder="páginasHTML")

@app.route("/")
def homepage():
    return render_template("pagina1.html")

@app.route("/etapa2")
def etapa2():
    return render_template("pagina2.html")

@app.route("/etapa3")
def etapa3():
    return render_template("pagina3.html")

@app.route("/etapa4")
def etapa4():
    return render_template("pagina4.html")

@app.route("/etapa5")
def etapa5():
    return render_template("pagina5.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8443, ssl_context="adhoc")