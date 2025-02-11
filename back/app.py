import requests
from flask import Flask, jsonify, request
from flask_cors import CORS  

app = Flask(__name__)

HOLIDAY_API_URL = 'https://date.nager.at/api/v3/PublicHolidays'

HEADERS = {
    "User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"
}

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/alerts', methods=['GET'])
def alerts():
    state = request.args.get('state', 'CA').strip()  # Valeur par défaut: 'CA'

    if not state:
        return jsonify({"error": "Le paramètre 'state' est requis."}), 400

    try:
        alerts_url = f"https://api.weather.gov/alerts/active?area={state}"
        response = requests.get(alerts_url, headers=HEADERS)
        print(f"Requête envoyée : {alerts_url}")
        print(f"Statut de la réponse : {response.status_code}")
        print(f"Contenu de la réponse : {response.text}")

        if response.status_code != 200:
            print(f"Erreur API : {response.text}")
            return jsonify({"error": f"L'API a retourné une erreur : {response.status_code}"}), response.status_code

        alerts_data = response.json()
        print(f"Données reçues de l'API : {alerts_data}")

        if "features" not in alerts_data or len(alerts_data["features"]) == 0:
            return jsonify({"message": f"Aucune alerte en cours pour l'État {state}"}), 200

        alert_list = [
            {
                "title": alert["properties"].get("headline", "Alerte sans titre"),
                "description": alert["properties"].get("description", "Pas de description disponible"),
                "severity": alert["properties"].get("severity", "Inconnue"),
                "urgency": alert["properties"].get("urgency", "Inconnue"),
                "areaDesc": alert["properties"].get("areaDesc", "Zone non précisée"),
                "effective": alert["properties"].get("effective", "Non précisé"),
                "expires": alert["properties"].get("expires", "Non précisé"),
            }
            for alert in alerts_data["features"]
        ]

        return jsonify(alert_list)

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de l'appel à l'API : {e}")
        return jsonify({"error": f"Erreur API : {e}"}), 500


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

