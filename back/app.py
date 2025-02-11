import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# User-Agent obligatoire pour Weather.gov
HEADERS = {
    "User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"
}

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/alerts', methods=['GET'])
def alerts():
    state = request.args.get('state', '').strip()  # État par défaut vide

    if not state:  # Vérifiez si le state est vide
        return jsonify({"error": "Le paramètre 'state' est requis."}), 400

    try:
        alerts_url = f"https://api.weather.gov/alerts/active?area={state}"
        response = requests.get(alerts_url, headers=HEADERS)
        response.raise_for_status()

        alerts_data = response.json()

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
        return jsonify({"error": f"Erreur API: {e}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)