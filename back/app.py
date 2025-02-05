<<<<<<< HEAD
from flask import Flask, render_template
from routes.nouvelles import get_articles

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/meteo')
def meteo():
    return render_template('index.html', content="Page Météo")

@app.route('/nouvelles')

def nouvelles():
    articles = get_articles()
    return render_template('nouvelles.html', articles=articles)  

@app.route('/calendrier')
def calendrier():
    return render_template('index.html', content="Page Calendrier")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001) 
=======
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# API externe à appeler (exemple)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> a020c03e567e7478fb470a947ba4e2a7ac1ab9d4
