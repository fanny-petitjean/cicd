import requests
from flask import Flask, jsonify
from flask_cors import CORS  # Pour autoriser le frontend à récupérer les données

app = Flask(__name__)
CORS(app)  # Permet au frontend d'accéder à l'API

def get_articles():
    url = "https://api.spaceflightnewsapi.net/v4/articles/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"][:5]  # On prend les 5 premiers articles
    return []


@app.route('/api/nouvelles')
def nouvelles():
    articles = get_articles()  # Appelle la fonction qui récupère les articles
    return jsonify(articles)  # Retourne les articles au format JSON

@app.route('/api/meteo')
def meteo():
    return jsonify({"message": "Données météo non disponibles pour l'instant."})

@app.route('/api/calendrier')
def calendrier():
    return jsonify({"message": "Fonctionnalité Calendrier en développement."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Backend sur le port 5000
