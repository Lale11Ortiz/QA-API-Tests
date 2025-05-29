import unittest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestJSONPlaceholderAPI(unittest.TestCase):

    def test_get_all_posts(self):
        response = requests.get(f"{BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        print("✅ GET all posts → OK")

if __name__ == "__main__":
    unittest.main()