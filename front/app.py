from flask import Flask, render_template, request
import requests
import logging

app = Flask(__name__)

# Configurer la journalisation
logging.basicConfig(level=logging.DEBUG)

# URL du backend (pointant vers le service Docker nommé "back")
BACKEND_URL = "http://back:5000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alertes', methods=['GET', 'POST'])
def alertes():
    state = "CA"  # Valeur par défaut
    if request.method == "POST":  # Si l'utilisateur soumet un état via le formulaire
        state = request.form.get("state", "CA").strip()

    try:
        # Envoie une requête au backend avec l'état
        response = requests.get(f"{BACKEND_URL}/api/alerts?state={state}")
        response.raise_for_status()  # Vérifie les erreurs HTTP
        alertes_data = response.json()  # Récupère les données JSON
        return render_template('alertes.html', alertes=alertes_data, state=state)
    except requests.exceptions.RequestException as e:
        # Gère les erreurs liées au backend
        return render_template('alertes.html', error=f"Erreur de connexion au backend : {e}", state=state)

@app.route('/nouvelles')
def nouvelles():
    return render_template('index.html', content="Page Nouvelles")

@app.route('/calendrier', methods=['GET'])
def calendrier():
    # Récupérer les paramètres du formulaire
    year = request.args.get('year', default=2025, type=int)
    country_code = request.args.get('countryCode', default='US', type=str).upper()

    try:
        # Appel au back-end pour récupérer les jours fériés
        response = requests.get(f"{BACKEND_URL}/api/calendrier", params={"year": year, "countryCode": country_code})

        if response.status_code == 200:
            holidays = response.json()  # Récupérer la réponse JSON du back-end
        else:
            holidays = [{"error": "Erreur lors de la récupération des jours fériés"}]
    
    except requests.exceptions.RequestException:
        holidays = [{"error": "Impossible de contacter le back-end"}]
    print(holidays)  # Affiche la variable 'holidays' dans la console

    # Retourner la page avec les résultats des jours fériés
    return render_template('calendrier.html', holidays=holidays)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)