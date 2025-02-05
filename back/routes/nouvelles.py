from flask import Blueprint, jsonify
import requests

def get_articles(limit=5):
    """Récupère les articles depuis l'API Spaceflight News"""
    url = "https://api.spaceflightnewsapi.net/v4/articles/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["results"][:limit]  # Récupère un nombre limité d'articles
    else:
        return []  # Retourne une liste vide en cas d'erreur
