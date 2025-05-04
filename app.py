from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_produits():
    with open("data/produits.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Services")
def services():
    return render_template("Services.html")


@app.route("/Nos Réalisations")
def realisations():
    return render_template("Nos Réalisations.html")

@app.route("/Produits/<int:id>")
def produit(id):
    produits = load_produits()
    produit = next((p for p in produits if p["id"] == id), None)
    return render_template("Produits.html", produit=produit)



if __name__ == "__main__":
    app.run(debug=True)
