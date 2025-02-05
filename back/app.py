import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

HOLIDAY_API_URL = 'https://date.nager.at/api/v3/PublicHolidays'

METEO_API_URL = 'https://api.meteo.com/v1/weather'
API_KEY = 'YOUR_API_KEY'

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/meteo')
def meteo():
    # Effectuer l'appel API vers le service météo
    response = requests.get(METEO_API_URL, params={'api_key': API_KEY, 'city': 'Paris'})
    
    if response.status_code == 200:
        # Traiter la réponse si elle est valide
        meteo_data = response.json()
        return jsonify(meteo_data)
    else:
        # Retourner une erreur si l'appel échoue
        return jsonify({'error': 'API météo non disponible'}), 500

@app.route('/api/calendrier')
def calendrier():
    # Récupérer les paramètres du formulaire
    year = request.args.get('year', default=2025, type=int)
    country_code = request.args.get('countryCode', default='FR', type=str).upper()  # Remplacer 'country' par 'countryCode'
    
    response = requests.get(f"{HOLIDAY_API_URL}/{year}/{country_code}")
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'API jours fériés non disponible'}), 500

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
