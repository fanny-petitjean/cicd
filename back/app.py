import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

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
        print(f"Requête envoyée à l'API : {alerts_url}")
        response = requests.get(alerts_url, headers=HEADERS)
        print(f"Statut de la réponse : {response.status_code}")

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)