import requests
from flask import Flask, jsonify, request
from flask_cors import CORS  

app = Flask(__name__)

HOLIDAY_API_URL = 'https://date.nager.at/api/v3/PublicHolidays'

METEO_API_URL = 'https://api.meteo.com/v1/weather'
API_KEY = 'YOUR_API_KEY'

NEWS_API_URL = "https://api.spaceflightnewsapi.net/v4/articles/"

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/meteo')
def meteo():
    response = requests.get(METEO_API_URL, params={'api_key': API_KEY, 'city': 'Paris'})
    
    if response.status_code == 200:
        meteo_data = response.json()
        return jsonify(meteo_data)
    else:
        return jsonify({'error': 'API météo non disponible'}), 500

@app.route('/api/calendrier')
def calendrier():
    year = request.args.get('year', default=2025, type=int)
    country_code = request.args.get('countryCode', default='FR', type=str).upper() 
    
    response = requests.get(f"{HOLIDAY_API_URL}/{year}/{country_code}")
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'API jours fériés non disponible'}), 500


import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Exemple de fonction qui récupère les actualités depuis une API externe
def fetch_news_data():
    url = "https://api.exemple.com/news"  # URL d'une API externe pour récupérer les actualités
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête a réussi
        return response.json()  # Retourne les données en format JSON
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des actualités : {e}")
        return []  # Retourne un tableau vide en cas d'erreur

@app.route("/api/news", methods=["GET"])
def get_articles():
    data = fetch_news_data()  # Appel de la fonction pour récupérer les données
    if data:
        return jsonify(data[:5])  # Limiter à 5 premiers articles
    else:
        return jsonify([])  # Retourner un tableau vide si aucune donnée n'est trouvée

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/api/news')
def get_articles():
    try:
        response = requests.get(NEWS_API_URL)
        
        if response.status_code == 200:
            data = response.json()  # C'est directement une liste d'articles

            # Retourner les 5 premiers articles
            return jsonify(data.get("articles", [])[:5])  # Assure-toi que "articles" existe et découpe la liste

        return jsonify({'error': f'Erreur API Spaceflight News - Code {response.status_code}'}), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Exception: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

