import requests
from flask import Flask, render_template, request

app = Flask(__name__)

BACKEND_URL = "http://back:5000"  # L'URL du backend dans Docker

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meteo')
def meteo():
    return render_template('index.html', content="Page Météo")

@app.route('/news')
def news():
    try:
        # Faire la requête pour récupérer les articles
        response = requests.get(f"{BACKEND_URL}/api/news")
        
        if response.status_code == 200:
            articles = response.json()  # Récupérer la réponse JSON
        else:
            articles = []
    except requests.exceptions.RequestException as e:
        articles = []
        print(f"Erreur lors de la récupération des articles : {e}")
    
    return render_template('news.html', articles=articles)

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
    app.run(host='0.0.0.0', port=5001)  # Frontend sur le port 5001
