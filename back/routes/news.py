import requests

def get_articles():
    url = "https://api.spaceflightnewsapi.net/v4/articles/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["results"][:5]  # On prend les 5 premiers articles
    return []
