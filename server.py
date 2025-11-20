from flask import Flask, render_template

app = Flask(__name__, template_folder="páginasHTML")

@app.route("/")
def pagina1():
    return render_template("main.html")

@app.route("/etapa2")
def pagina2():
    return render_template("pagina1.html")

@app.route("/etapa3")
def pagina3():
    return render_template("pagina2.html")

@app.route("/etapa4")
def pagina4():
    return render_template("pagina3.html")

@app.route("/etapa5")
def pagina5():
    return render_template("pagina4.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
