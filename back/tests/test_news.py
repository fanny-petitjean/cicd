import pytest
import requests_mock
from app import app

NEWS_API_URL = 'https://api.exemple.com/v1/news'  # Remplace par l'URL de ton API de news

@pytest.fixture
def client():
    """Fixture pour configurer un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_news_api_success(client):
    """Test API /api/news avec une réponse valide."""
    mock_response = [
        {"title": "Article 1", "summary": "Résumé de l'article 1", "image_url": "http://example.com/image1.jpg", "url": "http://example.com/article1"},
        {"title": "Article 2", "summary": "Résumé de l'article 2", "image_url": "http://example.com/image2.jpg", "url": "http://example.com/article2"}
    ]

    with requests_mock.Mocker() as m:
        m.get(NEWS_API_URL, json=mock_response, status_code=200)
        response = client.get('/api/news')

    assert response.status_code == 200
    assert response.json == mock_response


def test_news_api_failure(client):
    """Test API /api/news avec une erreur de l'API externe."""
    with requests_mock.Mocker() as m:
        m.get(NEWS_API_URL, status_code=500)
        response = client.get('/api/news')

    assert response.status_code == 500
    assert response.json == {"error": "API des actualités non disponible"}


def test_news_page(client):
    """Test de la page HTML avec la liste d'articles."""
    mock_response = [
        {"title": "Article 1", "summary": "Résumé de l'article 1", "image_url": "http://example.com/image1.jpg", "url": "http://example.com/article1"},
        {"title": "Article 2", "summary": "Résumé de l'article 2", "image_url": "http://example.com/image2.jpg", "url": "http://example.com/article2"}
    ]
    
    # Simule l'appel à l'API pour récupérer les articles
    with requests_mock.Mocker() as m:
        m.get(NEWS_API_URL, json=mock_response, status_code=200)
        response = client.get('/news')

    assert response.status_code == 200
    assert b"Article 1" in response.data
    assert b"Article 2" in response.data
    assert b"http://example.com/image1.jpg" in response.data
    assert b"http://example.com/image2.jpg" in response.data

#essai d'un nouveau test