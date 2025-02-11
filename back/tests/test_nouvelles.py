import unittest
from app import app

class TestNewsAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api_news(self):
        response = self.client.get('/api/news')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

if __name__ == '__main__':
    unittest.main()
