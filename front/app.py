from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL du backend (pointant vers le service Docker nommé "back")
BACKEND_URL = "http://back:5000"  # Nom du service Docker

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
        response = requests.get(f"{BACKEND_URL}?state={state}")
        response.raise_for_status()  # Vérifie les erreurs HTTP
        alertes_data = response.json()  # Récupère les données JSON
        return render_template('alertes.html', alertes=alertes_data, state=state)
    except requests.exceptions.RequestException as e:
        # Gère les erreurs liées au backend
        return render_template('alertes.html', error=f"Erreur de connexion au backend : {e}", state=state)

@app.route('/nouvelles')
def nouvelles():
    return render_template('index.html', content="Page Nouvelles")

@app.route('/calendrier')
def calendrier():
    return render_template('index.html', content="Page Calendrier")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)