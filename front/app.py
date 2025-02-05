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
