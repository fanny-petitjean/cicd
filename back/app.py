import requests
from flask import Flask, jsonify, request
from flask_cors import CORS  

app = Flask(__name__)

HOLIDAY_API_URL = 'https://date.nager.at/api/v3/PublicHolidays'

METEO_API_URL = 'https://api.meteo.com/v1/weather'
API_KEY = 'YOUR_API_KEY'

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

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

