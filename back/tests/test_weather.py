import pytest
import requests_mock
from app import app

METEO_API_URL = 'https://api.weather.gov/alerts/active'


@pytest.fixture
def client():
    """Fixture pour configurer un client de test Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_alerts_success(client):
    """Test API /api/alerts avec une réponse valide."""
    state = "CA"
    
    mock_response = {
        "features": [
            {
                "properties": {
                    "headline": "Alerte météo",
                    "description": "Fortes pluies attendues",
                    "severity": "Severe",
                    "urgency": "Immediate",
                    "areaDesc": "Los Angeles, CA",
                    "effective": "2025-02-11T10:00:00Z",
                    "expires": "2025-02-11T18:00:00Z"
                }
            }
        ]
    }

    with requests_mock.Mocker() as m:
        m.get(f"{METEO_API_URL}?area={state}", json=mock_response, status_code=200)
        response = client.get(f"/api/alerts?state={state}")

    assert response.status_code == 200
    assert response.json == [
        {
            "title": "Alerte météo",
            "description": "Fortes pluies attendues",
            "severity": "Severe",
            "urgency": "Immediate",
            "areaDesc": "Los Angeles, CA",
            "effective": "2025-02-11T10:00:00Z",
            "expires": "2025-02-11T18:00:00Z",
        }
    ]


def test_alerts_no_results(client):
    """Test API /api/alerts quand il n'y a pas d'alertes."""
    state = "NY"
    
    mock_response = {"features": []}

    with requests_mock.Mocker() as m:
        m.get(f"{METEO_API_URL}?area={state}", json=mock_response, status_code=200)
        response = client.get(f"/api/alerts?state={state}")

    assert response.status_code == 200
    assert response.json == {"message": f"Aucune alerte en cours pour l'État {state}"}


def test_alerts_api_failure(client):
    """Test API /api/alerts avec une erreur de l'API externe."""
    state = "CA"

    with requests_mock.Mocker() as m:
        m.get(f"{METEO_API_URL}?area={state}", status_code=500)
        response = client.get(f"/api/alerts?state={state}")

    assert response.status_code == 500
    assert response.json == {"error": "Erreur API : 500 Server Error: INTERNAL SERVER ERROR for url: https://api.weather.gov/alerts/active?area=CA"}