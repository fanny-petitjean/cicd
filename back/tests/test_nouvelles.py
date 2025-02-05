import unittest
from app import app

class TestNouvellesAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api_nouvelles(self):
        response = self.client.get('/api/nouvelles')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json) > 0)

if __name__ == '__main__':
    unittest.main()
