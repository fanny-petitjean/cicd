import pytest
import requests_mock
from app import app  # Import de ton application Flask

HOLIDAY_API_URL = 'https://date.nager.at/api/v3/PublicHolidays'


@pytest.fixture
def client():
    """Fixture pour configurer un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_calendrier_success(client):
    """Test API /api/calendrier avec une réponse valide."""
    year = 2025
    country = "FR"
    
    mock_response = [
        {"date": "2025-01-01", "localName": "Nouvel An", "name": "New Year's Day"},
        {"date": "2025-05-01", "localName": "Fête du Travail", "name": "Labour Day"}
    ]

    with requests_mock.Mocker() as m:
        m.get(f"{HOLIDAY_API_URL}/{year}/{country}", json=mock_response, status_code=200)
        response = client.get(f"/api/calendrier?year={year}&country={country}")

    assert response.status_code == 200
    assert response.json == mock_response


def test_calendrier_api_failure(client):
    """Test API /api/calendrier avec une erreur de l'API externe."""
    year = 2025
    country = "FR"

    with requests_mock.Mocker() as m:
        m.get(f"{HOLIDAY_API_URL}/{year}/{country}", status_code=500)
        response = client.get(f"/api/calendrier?year={year}&country={country}")

    assert response.status_code == 500
    assert response.json == {"error": "API jours fériés non disponible"}


def test_calendrier_invalid_country(client):
    """Test API /api/calendrier avec un code pays invalide."""
    response = client.get("/api/calendrier?year=2025&country=ZZ")  # Code invalide
    assert response.status_code == 500  # Vérifier qu'il y a bien une erreur


