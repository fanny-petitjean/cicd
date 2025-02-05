import requests
from flask import Flask, jsonify

app = Flask(__name__)

# API externe à appeler (exemple)
METEO_API_URL = 'https://api.meteo.com/v1/weather'
API_KEY = 'YOUR_API_KEY'

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
