import unittest
import requests

class TestNouvellesAPI(unittest.TestCase):
    def test_api_status_code(self):
        url = "https://api.spaceflightnewsapi.net/v4/articles/"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse est OK

    def test_articles_content(self):
        url = "https://api.spaceflightnewsapi.net/v4/articles/"
        response = requests.get(url)
        data = response.json()
        self.assertIn("results", data)  # Vérifie si les articles sont présents dans la réponse
        self.assertGreater(len(data["results"]), 0)  # Vérifie qu'il y a des articles

if __name__ == '__main__':
    unittest.main()
